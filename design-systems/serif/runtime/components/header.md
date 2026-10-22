<!-- Generated from index.html#component-header. Edit index.html, not this file. -->

## S-H01・H02｜上見出し型と左見出し型

横に広い部品を使うときは上見出し型、表や説明を右側へ置くときは左見出し型を出発点にします。表紙・目次・中扉・ミッション・エンドへ同じヘッダーを自動追加しません。

[見本SVG](header.svg)

上見出し：欧文14px＋日本語36px、いずれもRegular。

[見本SVG](sidebar.svg)

左見出し：欧文・日本語・細い短線・番号を縦に組む。

| 要素 | 800×450の観察値 | 長文への対応（提案） |
| --- | --- | --- |
| 上見出しの欧文 | x42 / y22、14px / 基準線41.4 | 役割を保って簡潔な表記にする。 |
| 日本語見出し | x42 / y50、36px / 基準線93.57 | 36→34→32、行送り54、最大2行。本文を下へ送る。 |
| 左見出し | x36、基準線82.4と134.57、短線y168 | 右の本文領域x298〜768と分離。 |
| ロゴ | x660 / y20 / w104 / h28 | 本文見出しの右端646を初期目安とし、ロゴと14px空ける。 |

ロゴ枠と見出しの長文処理は雛形の拡張です。色は配色と背景の局所的な明るさから決めます。白版・カラー版の両方が読みにくい場合だけ、紙色の面をロゴの下へ置きます。

仕様データ

```
{
  "id": "S-H01/H02",
  "native_canvas": [
    800,
    450
  ],
  "stack": {
    "x": 42,
    "label": {
      "y": 22,
      "size": 14,
      "font": "Libre Baskerville",
      "weight": 400,
      "baseline": 41.4
    },
    "title": {
      "y": 50,
      "size": 36,
      "font": "Noto Serif JP",
      "weight": 400,
      "baseline": 93.57
    }
  },
  "sidebar": {
    "x": 36,
    "english_baseline": 82.4,
    "japanese_baseline": 134.57,
    "hairline": [
      36,
      168,
      34,
      0.5
    ],
    "number": {
      "size": 25,
      "baseline": 200.75
    }
  },
  "running_company": {
    "chapter_x": 38,
    "chapter_baseline": 32.45,
    "mission_x": 42,
    "mission_baseline": 35.45,
    "size": 8,
    "font": "Noto Sans JP"
  },
  "logo": {
    "box": [
      680,
      20,
      84,
      23
    ],
    "plate": false,
    "asset_policy": "不要な外側余白をトリミングし、透過背景を保持。白い下地を追加しない。",
    "basis": "雛形で追加した独立領域。表示幅を104pxから84pxへ縮小し、右端764pxを維持。正式ロゴの色・縦横比は変更しない。"
  },
  "proposed": {
    "text_right": 646,
    "title_width": 604,
    "title_steps": [
      36,
      34,
      32
    ],
    "max_lines": 2,
    "line_height": 54,
    "body_min_y": 122,
    "title_body_gap": 18
  },
  "omit_stack_on": [
    "cover",
    "contents",
    "section",
    "mission",
    "closing"
  ]
}
```
