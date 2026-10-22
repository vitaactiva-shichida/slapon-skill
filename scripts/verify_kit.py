"""Check a customer-held code against a public, opaque license registry.

This is a possession check for the supported skill entrypoint, not DRM or a
restriction on reading public GitHub files. Never send the code to GitHub.
"""
import argparse
import hashlib
import hmac
import json
from pathlib import Path


def binding(license):
    fields = {key: license[key] for key in
              ('license_id', 'customer_id', 'compatibility_major', 'design_system', 'code')}
    return hashlib.sha256(json.dumps(fields, sort_keys=True, separators=(',', ':'),
                                     ensure_ascii=False).encode()).hexdigest()


def verify(customer, license, registry):
    """Return non-secret evidence, or fail closed without echoing input."""
    try:
        runtime = customer['runtime']
        if registry['schema_version'] != 1 or license['schema_version'] != 1:
            raise ValueError('Unsupported license schema')
        if (license['customer_id'], license['compatibility_major'], license['design_system']) != (
                customer['id'], runtime['compatibility_major'], runtime['design_system']):
            raise ValueError('License does not match this kit')
        if not isinstance(license['code'], str) or len(license['code']) < 32:
            raise ValueError('Missing or invalid kit code')
        record = registry['licenses'][license['license_id']]
        if record['status'] != 'active':
            raise ValueError('Kit code is inactive')
        if not hmac.compare_digest(binding(license), record['binding_sha256']):
            raise ValueError('Invalid kit code')
    except (KeyError, TypeError) as exc:
        raise ValueError('Missing or invalid kit license') from exc
    return dict(valid=True, license_id=license['license_id'], customer_id=customer['id'],
                compatibility_major=runtime['compatibility_major'], design_system=runtime['design_system'])


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--customer', type=Path, required=True)
    ap.add_argument('--license', type=Path, required=True)
    ap.add_argument('--registry', type=Path, required=True)
    args = ap.parse_args()
    try:
        print(json.dumps(verify(*[json.loads(p.read_text()) for p in
                                 [args.customer, args.license, args.registry]])))
    except (ValueError, OSError) as exc:
        ap.exit(2, str(exc)+'\n')
