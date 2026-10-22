<!-- Generated from index.html#typography. Edit index.html, not this file. -->

## 04 — 文字の階層・行送り・長文の処理

和文はNoto Sans JP、欧文の大見出しと独立した数字はArimo。400／500／700を役割で使い分けます。文字サイズは1600×900の参照pxで記録します。PowerPointが13⅓×7.5インチなら1px＝0.6ptです。

| ID・役割 | 書体 | サイズ / 行送り | 太さ | 収め方 |
| --- | --- | --- | --- | --- |
| C-T-COVER / 表紙・欧文 | Arimo | 100 / 116 | 700 | 100 → 96 → 88 / 最大2行 |
| C-T-CHAPTER / 中扉・欧文 | Arimo | 96 / 120 | 400 | 96 → 88 → 80 / 最大2行 |
| C-T01 / 本文見出し | Noto Sans JP | 44 / 64 | 700 | 44 → 40 → 36 / 最大2行 |
| C-T02 / 小見出し | Noto Sans JP | 28 / 42 | 700 | 役割内で統一 |
| C-T03 / 本文 | Noto Sans JP | 20 / 32 | 400 | 事業カード等の実値。新規投影資料は24〜28pxを候補に情報量を減らす |
| C-T04 / 人物・工程の詳細 | Noto Sans JP | 17 / 28 | 400 | 役割内で統一 |
| C-T05 / ラベル・注記 | Noto Sans JP | 14 / 22 | 400 | 役割内で統一 |
| C-T06 / ヘッダーのラベル | Noto Sans JP | 16 / 24 | 500 | 役割内で統一 |
| C-T07 / フッター | Noto Sans JP | 14 / 22 | 400 | 役割内で統一 |
| C-T-KPI / 数値 | Arimo | 48 / 58 | 700 | 原本48。行送り58は新規部品の提案 |
| C-T-NUMBER / 目次番号 | Arimo | 72 / 88 | 400 | 役割内で統一 |

[見本SVG](inline-previews/a9240de29308ea19fec3.svg)

文字階層の見本。64pxを超える表紙・中扉の文字はこの部品見本内だけ64pxへ縮めて表示し、上表の実値を優先。

原本の本文20pxはPowerPointで12pt、人物紹介17pxは10.2ptです。配布用の原本値と、遠くから見る資料の推奨値を分けます。投影では本文24〜28px、行送り36〜42pxを初期候補にし、情報を削るか分割して領域を確保します。

同じフォント・太さ・色の文章は、改行を含む一つのテキストボックスにまとめます。太字など一部だけ異なる場合は同じボックスのrunで表現。行の見かけだけをそろえるために文章を別々のボックスへ分割しません。代替書体を使った場合は改行・数字幅・文字切れを再確認します。

原本全ページのフォント実測一覧

| 書体 | 元px | PPT pt |
| --- | --- | --- |
| Arimo | 20.0 | 12.0 |
| Arimo | 24.0 | 14.4 |
| Arimo | 48.0 | 28.8 |
| Arimo | 72.0 | 43.2 |
| Arimo | 90.0 | 54.0 |
| Arimo | 96.0 | 57.6 |
| Arimo | 100.0 | 60.0 |
| Arimo | 240.0 | 144.0 |
| Noto Sans JP | 14.0 | 8.4 |
| Noto Sans JP | 16.0 | 9.6 |
| Noto Sans JP | 17.0 | 10.2 |
| Noto Sans JP | 18.0 | 10.8 |
| Noto Sans JP | 20.0 | 12.0 |
| Noto Sans JP | 22.0 | 13.2 |
| Noto Sans JP | 23.0 | 13.8 |
| Noto Sans JP | 24.0 | 14.4 |
| Noto Sans JP | 25.0 | 15.0 |
| Noto Sans JP | 27.0 | 16.2 |
| Noto Sans JP | 28.0 | 16.8 |
| Noto Sans JP | 30.0 | 18.0 |
| Noto Sans JP | 33.0 | 19.8 |
| Noto Sans JP | 40.0 | 24.0 |
| Noto Sans JP | 44.0 | 26.4 |

仕様データ

```
{
  "canvas": [
    1600,
    900
  ],
  "unit": "reference_px",
  "jp": "Noto Sans JP",
  "latin": "Arimo",
  "fallback": [
    "Yu Gothic",
    "Arial"
  ],
  "ppt_conversion": "px × slide_width_pt / 1600。960pt幅なら×0.6。",
  "roles": [
    {
      "id": "C-T-COVER",
      "name": "表紙・欧文",
      "font": "Arimo",
      "size": 100,
      "leading": 116,
      "weight": 700,
      "steps": [
        100,
        96,
        88
      ],
      "max_lines": 2,
      "basis": "原本100/116。縮小段階は提案"
    },
    {
      "id": "C-T-CHAPTER",
      "name": "中扉・欧文",
      "font": "Arimo",
      "size": 96,
      "leading": 120,
      "weight": 400,
      "steps": [
        96,
        88,
        80
      ],
      "max_lines": 2,
      "basis": "原本96/120。縮小段階は提案"
    },
    {
      "id": "C-T01",
      "name": "本文見出し",
      "font": "Noto Sans JP",
      "size": 44,
      "leading": 64,
      "weight": 700,
      "steps": [
        44,
        40,
        36
      ],
      "max_lines": 2,
      "basis": "原本44/64。長文処理は提案"
    },
    {
      "id": "C-T02",
      "name": "小見出し",
      "font": "Noto Sans JP",
      "size": 28,
      "leading": 42,
      "weight": 700
    },
    {
      "id": "C-T03",
      "name": "本文",
      "font": "Noto Sans JP",
      "size": 20,
      "leading": 32,
      "weight": 400,
      "basis": "事業カード等の実値。新規投影資料は24〜28pxを候補に情報量を減らす"
    },
    {
      "id": "C-T04",
      "name": "人物・工程の詳細",
      "font": "Noto Sans JP",
      "size": 17,
      "leading": 28,
      "weight": 400
    },
    {
      "id": "C-T05",
      "name": "ラベル・注記",
      "font": "Noto Sans JP",
      "size": 14,
      "leading": 22,
      "weight": 400
    },
    {
      "id": "C-T06",
      "name": "ヘッダーのラベル",
      "font": "Noto Sans JP",
      "size": 16,
      "leading": 24,
      "weight": 500
    },
    {
      "id": "C-T07",
      "name": "フッター",
      "font": "Noto Sans JP",
      "size": 14,
      "leading": 22,
      "weight": 400
    },
    {
      "id": "C-T-KPI",
      "name": "数値",
      "font": "Arimo",
      "size": 48,
      "leading": 58,
      "weight": 700,
      "basis": "原本48。行送り58は新規部品の提案"
    },
    {
      "id": "C-T-NUMBER",
      "name": "目次番号",
      "font": "Arimo",
      "size": 72,
      "leading": 88,
      "weight": 400
    }
  ],
  "paragraph_policy": "同一書式の段落は一つのテキストボックス。行ごとの分割はしない。部分的な強調は同一ボックス内のrunで保持。",
  "source_policy": "原本の小さい文字を通常本文の標準にしない。投影と配布の用途を分け、文字サイズの前に情報量を調整。",
  "drawing": {
    "id": "type-ladder",
    "title": "Companyの文字階層",
    "canvas": [
      1600,
      889
    ],
    "nodes": [
      {
        "type": "rect",
        "x": 0,
        "y": 0,
        "w": 1600,
        "h": 889,
        "fill_role": "background"
      },
      {
        "type": "text",
        "x": 40,
        "y": 24,
        "w": 400,
        "h": 50,
        "text": "C-T-COVER / 100px",
        "size": 22,
        "leading": 33.0,
        "fill_role": "muted",
        "weight": 400
      },
      {
        "type": "text",
        "x": 460,
        "y": 24,
        "w": 1090,
        "h": 232,
        "text": "Business Impact",
        "size": 64,
        "leading": 78,
        "fill_role": "text",
        "weight": 700,
        "font": "Arimo"
      },
      {
        "type": "text",
        "x": 40,
        "y": 128,
        "w": 400,
        "h": 50,
        "text": "C-T-CHAPTER / 96px",
        "size": 22,
        "leading": 33.0,
        "fill_role": "muted",
        "weight": 400
      },
      {
        "type": "text",
        "x": 460,
        "y": 128,
        "w": 1090,
        "h": 240,
        "text": "Business Impact",
        "size": 64,
        "leading": 78,
        "fill_role": "text",
        "weight": 400,
        "font": "Arimo"
      },
      {
        "type": "text",
        "x": 40,
        "y": 232,
        "w": 400,
        "h": 50,
        "text": "C-T01 / 44px",
        "size": 22,
        "leading": 33.0,
        "fill_role": "muted",
        "weight": 400
      },
      {
        "type": "text",
        "x": 460,
        "y": 232,
        "w": 1090,
        "h": 128,
        "text": "本文見出し：情報を明快に伝える。",
        "size": 44,
        "leading": 64,
        "fill_role": "text",
        "weight": 700,
        "font": "Noto Sans JP"
      },
      {
        "type": "text",
        "x": 40,
        "y": 323,
        "w": 400,
        "h": 50,
        "text": "C-T02 / 28px",
        "size": 22,
        "leading": 33.0,
        "fill_role": "muted",
        "weight": 400
      },
      {
        "type": "text",
        "x": 460,
        "y": 323,
        "w": 1090,
        "h": 84,
        "text": "小見出し：情報を明快に伝える。",
        "size": 28,
        "leading": 42,
        "fill_role": "text",
        "weight": 700,
        "font": "Noto Sans JP"
      },
      {
        "type": "text",
        "x": 40,
        "y": 414,
        "w": 400,
        "h": 50,
        "text": "C-T03 / 20px",
        "size": 22,
        "leading": 33.0,
        "fill_role": "muted",
        "weight": 400
      },
      {
        "type": "text",
        "x": 460,
        "y": 414,
        "w": 1090,
        "h": 65,
        "text": "本文：情報を明快に伝える。",
        "size": 20,
        "leading": 32,
        "fill_role": "text",
        "weight": 400,
        "font": "Noto Sans JP"
      },
      {
        "type": "text",
        "x": 40,
        "y": 505,
        "w": 400,
        "h": 50,
        "text": "C-T04 / 17px",
        "size": 22,
        "leading": 33.0,
        "fill_role": "muted",
        "weight": 400
      },
      {
        "type": "text",
        "x": 460,
        "y": 505,
        "w": 1090,
        "h": 65,
        "text": "人物・工程の詳細：情報を明快に伝える。",
        "size": 17,
        "leading": 28,
        "fill_role": "text",
        "weight": 400,
        "font": "Noto Sans JP"
      },
      {
        "type": "text",
        "x": 40,
        "y": 596,
        "w": 400,
        "h": 50,
        "text": "C-T05 / 14px",
        "size": 22,
        "leading": 33.0,
        "fill_role": "muted",
        "weight": 400
      },
      {
        "type": "text",
        "x": 460,
        "y": 596,
        "w": 1090,
        "h": 65,
        "text": "ラベル・注記：情報を明快に伝える。",
        "size": 14,
        "leading": 22,
        "fill_role": "text",
        "weight": 400,
        "font": "Noto Sans JP"
      },
      {
        "type": "text",
        "x": 40,
        "y": 687,
        "w": 400,
        "h": 50,
        "text": "C-T06 / 16px",
        "size": 22,
        "leading": 33.0,
        "fill_role": "muted",
        "weight": 400
      },
      {
        "type": "text",
        "x": 460,
        "y": 687,
        "w": 1090,
        "h": 65,
        "text": "ヘッダーのラベル：情報を明快に伝える。",
        "size": 16,
        "leading": 24,
        "fill_role": "text",
        "weight": 500,
        "font": "Noto Sans JP"
      },
      {
        "type": "text",
        "x": 40,
        "y": 778,
        "w": 400,
        "h": 50,
        "text": "C-T07 / 14px",
        "size": 22,
        "leading": 33.0,
        "fill_role": "muted",
        "weight": 400
      },
      {
        "type": "text",
        "x": 460,
        "y": 778,
        "w": 1090,
        "h": 65,
        "text": "フッター：情報を明快に伝える。",
        "size": 14,
        "leading": 22,
        "fill_role": "text",
        "weight": 400,
        "font": "Noto Sans JP"
      }
    ]
  }
}
```
