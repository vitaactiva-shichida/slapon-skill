<!-- Generated from index.html#component-footer. Edit index.html, not this file. -->

## S-F01｜罫線・発行元・ページ番号

[見本SVG](footer-light.svg)

本文：紙色の面に配色のmuted。

[見本SVG](footer-color.svg)

中扉：背景と一組の文字色・罫線色。

| 要素 | 基準 | 運用 |
| --- | --- | --- |
| 本文の罫線 | x26 / y415 / w748 / h0.5 | 画面端まで延長せず、左右26pxを保持。 |
| 発行元 | x26 / 基準線429.95 / 8px | 正式社名。本文や出典と別の編集単位。 |
| ページ番号 | 右端774 / 基準線429.95 / 8px | 桁数にかかわらず右アンカーを保持。 |
| 表紙 | 罫線y393、日付基準線407.95 | 本文用のフッターを重ねない。 |
| 新規本文・出典 | 本文下端396、出典基準線406を初期目安 | 出典が長いなら本文領域を減らす。原本の節目説明は固有の例外。 |

仕様データ

```
{
  "id": "S-F01",
  "observed": {
    "line": [
      26,
      415,
      748,
      0.5
    ],
    "company": {
      "x": 26,
      "baseline": 429.95,
      "size": 8
    },
    "page": {
      "right": 774,
      "baseline": 429.95,
      "size": 8
    },
    "cover": {
      "line_y": 393,
      "date_baseline": 407.95
    }
  },
  "proposed": {
    "body_bottom": 396,
    "source_note": {
      "x": 42,
      "baseline": 406,
      "size": 8,
      "max_right": 758
    }
  },
  "palette_policy": "本文は配色のmuted、濃い面は対応する文字色。左と右の直下の背景を別々に確認。",
  "source_exception": "原本実績ページの節目説明は基準線407.8。新原稿の標準下端と区別。"
}
```
