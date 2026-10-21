"""Search the catalog and export a selected SVG/PNG pair; no image generation."""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import struct
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "assets/design-patterns/catalog.json"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def positive(value):
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("Must be positive")
    return number


def load_catalog():
    raw = CATALOG.read_bytes()
    data = json.loads(raw)
    if not isinstance(data, dict) or data.get("schema_version") != 1 or not isinstance(data.get("patterns"), list):
        raise ValueError("Unsupported catalog schema")
    ids = set()
    for pattern in data["patterns"]:
        identifier = pattern["id"]
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", identifier) or identifier in ids:
            raise ValueError("Invalid or duplicate pattern ID: " + identifier)
        ids.add(identifier)
        if not isinstance(pattern["elements"], int) or pattern["elements"] < 1:
            raise ValueError("Invalid elements: " + identifier)
        if pattern["information_density"] not in {"low", "medium", "high"}:
            raise ValueError("Invalid density: " + identifier)
        for key in ("tags", "use_when", "cautions"):
            if not isinstance(pattern[key], list) or not all(isinstance(x, str) for x in pattern[key]):
                raise ValueError("Invalid " + key + ": " + identifier)
        for kind in ("svg", "png"):
            record = pattern["assets"][kind]
            if not re.fullmatch(r"[0-9a-f]{64}", record["sha256"]):
                raise ValueError("Invalid asset hash: " + identifier)
    return data["patterns"], digest(raw)


def read_asset(record, kind):
    relative = Path(record["path"])
    path = (ROOT / relative).resolve()
    asset_root = (ROOT / "assets/design-patterns").resolve()
    if relative.is_absolute() or not path.is_relative_to(asset_root) or not path.is_file():
        raise ValueError("Missing or outside asset: " + str(relative))
    if path.suffix != "." + kind:
        raise ValueError("Unexpected asset format: " + str(relative))
    raw = path.read_bytes()
    if digest(raw) != record["sha256"]:
        raise ValueError("Asset hash mismatch: " + str(relative))
    if kind == "svg":
        if ET.fromstring(raw).tag != "{http://www.w3.org/2000/svg}svg":
            raise ValueError("Invalid SVG: " + str(relative))
    elif len(raw) < 33 or raw[:8] != b"\x89PNG\r\n\x1a\n" or raw[12:16] != b"IHDR":
        raise ValueError("Invalid PNG: " + str(relative))
    return path, raw


def search(patterns, args):
    terms = args.query.casefold().split()
    matches = []
    for pattern in patterns:
        if args.id and pattern["id"] != args.id:
            continue
        if args.direction and pattern["direction"] != args.direction:
            continue
        if args.elements and pattern["elements"] != args.elements:
            continue
        if args.density and pattern["information_density"] != args.density:
            continue
        haystack = " ".join([
            pattern["id"], pattern["name"], pattern["direction"],
            pattern.get("element_kind", ""), *pattern["tags"], *pattern["use_when"],
        ]).casefold()
        if all(term in haystack for term in terms):
            matches.append(pattern)
    return matches


def describe(pattern):
    svg, _ = read_asset(pattern["assets"]["svg"], "svg")
    png, _ = read_asset(pattern["assets"]["png"], "png")
    return dict(pattern, attachment_paths=[str(png)], svg_path=str(svg))


def export_pattern(pattern, output_dir, catalog_hash):
    payloads = {}
    files = {}
    for kind in ("svg", "png"):
        _, raw = read_asset(pattern["assets"][kind], kind)
        name = "preview." + kind
        payloads[name] = raw
        files[kind] = {"path": name, "sha256": digest(raw)}
    manifest = {
        "schema_version": 1,
        "catalog_sha256": catalog_hash,
        "pattern": pattern,
        "files": files,
    }
    payloads["pattern.json"] = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode()
    parent = Path(output_dir).resolve()
    target = (parent / pattern["id"]).resolve()
    if not target.is_relative_to(parent):
        raise ValueError("Export directory escapes output location")
    # Verify both inputs and every existing output before writing any files.
    for name, raw in payloads.items():
        file = target / name
        if not file.resolve().is_relative_to(target):
            raise ValueError("Export file escapes output location: " + name)
        if file.exists() and file.read_bytes() != raw:
            raise ValueError("Existing output differs; choose a new output directory: " + str(file))
    target.mkdir(parents=True, exist_ok=True)
    for name, raw in payloads.items():
        file = target / name
        if not file.exists():
            file.write_bytes(raw)
    return {
        "svg_path": str(target / "preview.svg"),
        "attachment_paths": [str(target / "preview.png")],
        "export_manifest": str(target / "pattern.json"),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--direction", help="Direction; unknown values return no matches")
    parser.add_argument("--elements", type=positive)
    parser.add_argument("--density", choices=["low", "medium", "high"])
    parser.add_argument("--query", default="", help="Whitespace-separated terms, combined with AND")
    parser.add_argument("--id", help="Exact pattern ID")
    parser.add_argument("--limit", type=positive, default=3)
    parser.add_argument("--output-dir", help="Export only the pattern selected with --id")
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--validate", action="store_true")
    action.add_argument("--list-directions", action="store_true")
    args = parser.parse_args()
    if args.output_dir and (not args.id or args.validate or args.list_directions):
        parser.error("--output-dir requires --id and cannot be used with validation or listing")
    try:
        patterns, catalog_hash = load_catalog()
        if args.list_directions:
            result = dict(sorted(Counter(p["direction"] for p in patterns).items()))
        elif args.validate:
            for pattern in patterns:
                read_asset(pattern["assets"]["svg"], "svg")
                _, png = read_asset(pattern["assets"]["png"], "png")
                actual = struct.unpack(">II", png[16:24])
                expected = (pattern["canvas"]["width"], pattern["canvas"]["height"])
                if actual != expected:
                    raise ValueError("PNG dimensions differ from catalog: " + pattern["id"])
            result = {"valid": True, "patterns": len(patterns), "svg_files": len(patterns), "png_files": len(patterns)}
        else:
            matches = search(patterns, args)
            if args.output_dir and len(matches) != 1:
                raise ValueError("No pattern matches the requested ID and filters")
            results = [describe(p) for p in matches[:args.limit]]
            if args.output_dir:
                results[0].update(export_pattern(matches[0], args.output_dir, catalog_hash))
            result = {"schema_version": 1, "catalog_sha256": catalog_hash, "total": len(matches), "results": results}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, OSError, KeyError, TypeError, ET.ParseError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
