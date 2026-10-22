<!-- Generated from index.html#typography. Edit index.html, not this file. -->

## 04 — 明朝体・欧文セリフ・本文ゴシック

日本語の見出し・氏名・表はNoto Serif JP、欧文と独立した主役の数字はLibre Baskerville、長い説明と注記はNoto Sans JPを使います。原本はいずれもRegular 400です。見出しを一律にBoldへ変更しません。

| 役割 | 書体 | 元px / 行送り | 観察／設定 |
| --- | --- | --- | --- |
| S-T-COVER 表紙・欧文 | Libre Baskerville | 74 / 83 | 原本の2行の基準線差83 |
| S-T-CHAPTER 中扉・エンドの欧文 | Libre Baskerville | 56 / 65 | 中扉の基準線差65。エンドは単行 |
| S-T01 日本語見出し | Noto Serif JP | 36 / 54 | 原本サイズ36。行送り54は長文時の設定用の目安 |
| S-T02 人物名 | Noto Serif JP | 21 / 31.5 | 原本21、単行の行送りは提案 |
| S-T03 欧文ラベル | Libre Baskerville | 14 / 22 | 原本14、単行の行送りは提案 |
| S-T04 本文 | Noto Sans JP | 11 / 18 | ミッションの実値 |
| S-T05 プロフィール・工程説明 | Noto Sans JP | 10 / 15.5 | 原本の複数行基準線差15.5 |
| S-T06 表の項目・値 | Noto Serif JP | 14 / 21 | 原本14、複数行の行送りは提案 |
| S-T07 フッター・小ラベル | Noto Sans JP | 8 / 12.5 | フッターは単行。KPIのラベルは基準線差12.5 |
| S-T-KPI 数値 | Libre Baskerville | 22 / 30 | KPI22、実績指標28。単行の行送りは提案 |

[見本SVG](inline-previews/b0c524ba400bfb636a26.svg)

800px幅の座標で書体とサイズを比較。ラベルは役割の説明、見本文字は各役割の実サイズ。

Serifの元座標は800×450です。13⅓×7.5インチのPowerPointへは元px×1.2でポイントへ換算します。36pxは43.2pt、10pxは12ptです。CompanyやStandardの1600×900の数値と混ぜません。

原本の9.5〜11pxは配布用の説明の実値です。投影資料では12〜14px・行送り19〜22pxを初期候補にし、文章量やカラムを見直します。注記サイズを通常本文に転用しません。

同じ書体・太さ・色の段落は一つのテキストボックスにまとめ、改行はボックス内へ保持します。一部の強調は同一ボックス内の書式として扱います。代替書体はYu Mincho／Georgia、説明文はYu Gothic／Arialを候補にし、改行・数字の幅・はみ出しを確認します。

原本の文字サイズ一覧

| 書体 | 元px | PPT pt |
| --- | --- | --- |
| Libre Baskerville | 14.0 | 16.8 |
| Libre Baskerville | 16.0 | 19.2 |
| Libre Baskerville | 20.0 | 24.0 |
| Libre Baskerville | 22.0 | 26.4 |
| Libre Baskerville | 25.0 | 30.0 |
| Libre Baskerville | 28.0 | 33.6 |
| Libre Baskerville | 48.0 | 57.6 |
| Libre Baskerville | 56.0 | 67.2 |
| Libre Baskerville | 74.0 | 88.8 |
| Libre Baskerville | 110.0 | 132.0 |
| Noto Sans JP | 7.0 | 8.4 |
| Noto Sans JP | 8.0 | 9.6 |
| Noto Sans JP | 9.5 | 11.4 |
| Noto Sans JP | 10.0 | 12.0 |
| Noto Sans JP | 11.0 | 13.2 |
| Noto Serif JP | 13.0 | 15.6 |
| Noto Serif JP | 14.0 | 16.8 |
| Noto Serif JP | 15.0 | 18.0 |
| Noto Serif JP | 19.0 | 22.8 |
| Noto Serif JP | 21.0 | 25.2 |
| Noto Serif JP | 24.0 | 28.8 |
| Noto Serif JP | 26.0 | 31.2 |
| Noto Serif JP | 36.0 | 43.2 |

仕様データ

```
{
  "canvas": [
    800,
    450
  ],
  "unit": "source_px",
  "ppt_conversion": "13⅓×7.5インチ＝960×540pt。元px×1.2。1600×900へ拡大した値なら×0.6。",
  "roles": [
    {
      "id": "S-T-COVER",
      "role": "表紙・欧文",
      "font": "Libre Baskerville",
      "size": 74,
      "leading": 83,
      "weight": 400,
      "basis": "原本の2行の基準線差83"
    },
    {
      "id": "S-T-CHAPTER",
      "role": "中扉・エンドの欧文",
      "font": "Libre Baskerville",
      "size": 56,
      "leading": 65,
      "weight": 400,
      "basis": "中扉の基準線差65。エンドは単行"
    },
    {
      "id": "S-T01",
      "role": "日本語見出し",
      "font": "Noto Serif JP",
      "size": 36,
      "leading": 54,
      "weight": 400,
      "basis": "原本サイズ36。行送り54は長文時の設定用の目安"
    },
    {
      "id": "S-T02",
      "role": "人物名",
      "font": "Noto Serif JP",
      "size": 21,
      "leading": 31.5,
      "weight": 400,
      "basis": "原本21、単行の行送りは提案"
    },
    {
      "id": "S-T03",
      "role": "欧文ラベル",
      "font": "Libre Baskerville",
      "size": 14,
      "leading": 22,
      "weight": 400,
      "basis": "原本14、単行の行送りは提案"
    },
    {
      "id": "S-T04",
      "role": "本文",
      "font": "Noto Sans JP",
      "size": 11,
      "leading": 18,
      "weight": 400,
      "basis": "ミッションの実値"
    },
    {
      "id": "S-T05",
      "role": "プロフィール・工程説明",
      "font": "Noto Sans JP",
      "size": 10,
      "leading": 15.5,
      "weight": 400,
      "basis": "原本の複数行基準線差15.5"
    },
    {
      "id": "S-T06",
      "role": "表の項目・値",
      "font": "Noto Serif JP",
      "size": 14,
      "leading": 21,
      "weight": 400,
      "basis": "原本14、複数行の行送りは提案"
    },
    {
      "id": "S-T07",
      "role": "フッター・小ラベル",
      "font": "Noto Sans JP",
      "size": 8,
      "leading": 12.5,
      "weight": 400,
      "basis": "フッターは単行。KPIのラベルは基準線差12.5"
    },
    {
      "id": "S-T-KPI",
      "role": "数値",
      "font": "Libre Baskerville",
      "size": 22,
      "leading": 30,
      "weight": 400,
      "basis": "KPI22、実績指標28。単行の行送りは提案"
    }
  ],
  "hierarchy": "見出しと主役の数値は明朝・欧文セリフ、長い説明と注記はゴシック。Boldを一括適用しない。",
  "projection_proposal": {
    "body_size": [
      12,
      14
    ],
    "body_leading": [
      19,
      22
    ],
    "basis": "新規投影資料向けの初期候補。情報量とレイアウトを再配分。"
  },
  "paragraph_policy": "同じ書式の段落は改行を含め一つのテキストボックス。部分的な強調は同一ボックス内の書式。",
  "drawing": {
    "id": "type-ladder",
    "title": "Serifの書体と文字階層",
    "canvas": [
      800,
      752
    ],
    "nodes": [
      {
        "type": "rect",
        "x": 0,
        "y": 0,
        "w": 800,
        "h": 752,
        "fill_role": "background"
      },
      {
        "type": "text",
        "x": 26,
        "y": 20,
        "w": 200,
        "h": 35,
        "text": "S-T-COVER / 74px",
        "size": 11,
        "leading": 16.5,
        "fill_role": "muted",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 240,
        "y": 20,
        "w": 534,
        "h": 166,
        "text": "Company",
        "size": 74,
        "leading": 83,
        "fill_role": "heading",
        "font": "Libre Baskerville",
        "weight": 400
      },
      {
        "type": "text",
        "x": 26,
        "y": 127,
        "w": 200,
        "h": 35,
        "text": "S-T-CHAPTER / 56px",
        "size": 11,
        "leading": 16.5,
        "fill_role": "muted",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 240,
        "y": 127,
        "w": 534,
        "h": 130,
        "text": "Company",
        "size": 56,
        "leading": 65,
        "fill_role": "heading",
        "font": "Libre Baskerville",
        "weight": 400
      },
      {
        "type": "text",
        "x": 26,
        "y": 216,
        "w": 200,
        "h": 35,
        "text": "S-T01 / 36px",
        "size": 11,
        "leading": 16.5,
        "fill_role": "muted",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 240,
        "y": 216,
        "w": 534,
        "h": 108,
        "text": "資料の本質を伝える。",
        "size": 36,
        "leading": 54,
        "fill_role": "heading",
        "font": "Noto Serif JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 26,
        "y": 294,
        "w": 200,
        "h": 35,
        "text": "S-T02 / 21px",
        "size": 11,
        "leading": 16.5,
        "fill_role": "muted",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 240,
        "y": 294,
        "w": 534,
        "h": 63.0,
        "text": "資料の本質を伝える。",
        "size": 21,
        "leading": 31.5,
        "fill_role": "heading",
        "font": "Noto Serif JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 26,
        "y": 358,
        "w": 200,
        "h": 35,
        "text": "S-T03 / 14px",
        "size": 11,
        "leading": 16.5,
        "fill_role": "muted",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 240,
        "y": 358,
        "w": 534,
        "h": 60,
        "text": "Company",
        "size": 14,
        "leading": 22,
        "fill_role": "heading",
        "font": "Libre Baskerville",
        "weight": 400
      },
      {
        "type": "text",
        "x": 26,
        "y": 422,
        "w": 200,
        "h": 35,
        "text": "S-T04 / 11px",
        "size": 11,
        "leading": 16.5,
        "fill_role": "muted",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 240,
        "y": 422,
        "w": 534,
        "h": 60,
        "text": "資料の本質を伝える。",
        "size": 11,
        "leading": 18,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 26,
        "y": 486,
        "w": 200,
        "h": 35,
        "text": "S-T05 / 10px",
        "size": 11,
        "leading": 16.5,
        "fill_role": "muted",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 240,
        "y": 486,
        "w": 534,
        "h": 60,
        "text": "資料の本質を伝える。",
        "size": 10,
        "leading": 15.5,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 26,
        "y": 550,
        "w": 200,
        "h": 35,
        "text": "S-T06 / 14px",
        "size": 11,
        "leading": 16.5,
        "fill_role": "muted",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 240,
        "y": 550,
        "w": 534,
        "h": 60,
        "text": "資料の本質を伝える。",
        "size": 14,
        "leading": 21,
        "fill_role": "heading",
        "font": "Noto Serif JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 26,
        "y": 614,
        "w": 200,
        "h": 35,
        "text": "S-T07 / 8px",
        "size": 11,
        "leading": 16.5,
        "fill_role": "muted",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 240,
        "y": 614,
        "w": 534,
        "h": 60,
        "text": "資料の本質を伝える。",
        "size": 8,
        "leading": 12.5,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 26,
        "y": 678,
        "w": 200,
        "h": 35,
        "text": "S-T-KPI / 22px",
        "size": 11,
        "leading": 16.5,
        "fill_role": "muted",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 240,
        "y": 678,
        "w": 534,
        "h": 60,
        "text": "72.5%",
        "size": 22,
        "leading": 30,
        "fill_role": "heading",
        "font": "Libre Baskerville",
        "weight": 400
      }
    ]
  }
}
```
