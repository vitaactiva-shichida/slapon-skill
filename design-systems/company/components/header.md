<!-- Generated from index.html#component-header. Edit index.html, not this file. -->

## C-H01｜ヘッダー：ラベル・見出し・ロゴ

Companyのヘッダーは英語ラベルと日本語のページ見出しを縦に組みます。見出しは本文の結論を示し、フッターの発行元やページ番号と分離します。

{{component.header}}

白・淡い背景：濃い見出しとカラー版ロゴ。

{{component.header-dark}}

背景色あり：onmainの文字と対応するロゴ版。ロゴは独立要素。

| 要素 | Companyの基準（参照px） | 収まらないとき |
| --- | --- | --- |
| ラベル | x80 / y42 / 16px Medium / 行送り24 / 基準線60.4 | 長いラベルは語を整理。表題とは別の役割を保つ。 |
| 見出し | x80 / y78 / 44px Bold / 行送り64 / 基準線127.6 | 新原稿は44→40→36px、最大2行を初期目安にする。 |
| ロゴ | x1330 / y40 / w190 / h52、等比内接 | 文字の右端1306までを目安にし、24pxの間隔を確保。 |
| 本文開始 | 1行ならy180を初期目安 | 見出しが2行なら、見出し下端＋38px以降へ本文を送る。説明文があればその下端＋32px。 |

ラベル・見出しの位置と基準線は原本からの観察値。ロゴ枠、長文のサイズ段階、本文開始の計算は雛形の運用提案です。既存見本の配置は保持し、新原稿へ適用します。

仕様データ

```
{
  "id": "C-H01",
  "observed": {
    "region": [
      80,
      42,
      1440,
      100
    ],
    "label": {
      "x": 80,
      "y": 42,
      "size": 16,
      "weight": 500,
      "leading": 24,
      "baseline": 60.4
    },
    "title": {
      "x": 80,
      "y": 78,
      "size": 44,
      "weight": 700,
      "leading": 64,
      "baseline": 127.6
    },
    "automatic_underline": false
  },
  "logo": {
    "box": [
      1368,
      40,
      152,
      42
    ],
    "status": "雛形で追加したロゴ領域。表示幅を190pxから152pxへ20%縮小し、右端1520pxを維持。",
    "fit": "contain, preserve aspect ratio",
    "clearance": 24,
    "plate": false,
    "asset_policy": "不要な外側余白をトリミングし、透過背景を保持。白い下地を追加しない。"
  },
  "proposed": {
    "text_max_right": 1306,
    "title_width": 1226,
    "title_size_steps": [
      44,
      40,
      36
    ],
    "title_max_lines": 2,
    "body_min_y": 180,
    "body_gap_after_title": 38,
    "subtitle_gap": 16,
    "body_gap_after_subtitle": 32
  },
  "variants": {
    "light": {
      "ink": "text",
      "label": "primaryInk",
      "logo": "color"
    },
    "tint": {
      "ink": "inkSurface",
      "label": "primaryInkSurface",
      "logo": "color"
    },
    "dark": {
      "ink": "onmain",
      "label": "onmain",
      "logo": "white when onmain is white"
    }
  },
  "omit_when": [
    "cover",
    "contents-side-heading",
    "section",
    "mission-special",
    "closing"
  ],
  "source_policy": "上のラベルはページ内の見出し。Standardの80pxパンくずバーや短い下線を自動追加しない。"
}
```
