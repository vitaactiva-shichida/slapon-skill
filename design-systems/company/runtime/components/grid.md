<!-- Generated from index.html#component-grid. Edit index.html, not this file. -->

## C-G01–G06｜カラム：幅・間隔・非対称の割付

左右80px、有効幅1440pxを12ユニットで割り付けます。Standardの考え方を使い、Companyでは24pxの間隔を基本にします。原本の3事業カードの464px幅と一致します。

| 計算 | 参照px |
| --- | --- |
| ユニット幅 | (1440 − 11×24) ÷ 12 = 98 |
| nユニットの幅 | n×98 ＋ (n−1)×24 |
| 開始位置 | 80 ＋ 開始ユニット数×122 |
| 縦方向の初期目安 | 本文y300〜820。説明文や出典に応じて再配分 |

[見本SVG](../inline-previews/c2a4c742f0afb103818d.svg)

同じグリッドを背景なし・カードなしでも使用。4つの背景パターンとカラム数は独立して選ぶ。

| 構成 | 列のx / 幅 |
| --- | --- |
| C-G01 1カラム | x80 / w1440.0 |
| C-G02 2カラム | x80 / w708.0 ／ x812.0 / w708.0 |
| C-G03 3カラム | x80 / w464.0 ／ x568.0 / w464.0 ／ x1056.0 / w464.0 |
| C-G04 4カラム | x80 / w342.0 ／ x446.0 / w342.0 ／ x812.0 / w342.0 ／ x1178.0 / w342.0 |
| C-G05 左1：右2 | x80 / w464.0 ／ x568.0 / w952.0 |
| C-G06 左2：右1 | x80 / w952.0 ／ x1056.0 / w464.0 |

原本の人物紹介はx80と840から始まる固有の2列、KPIは幅960内に228px×4列・間隔16pxという別の割付です。既存の作例を12ユニットへ強制的に正規化しません。新原稿で同じ役割の列を比較するときは、見出し・本文・数値の位置と文字サイズをそろえます。

仕様データ

```
{
  "canvas": [
    1600,
    900
  ],
  "left": 80,
  "right": 1520,
  "width": 1440,
  "units": 12,
  "gutter": 24,
  "unit_width": 98.0,
  "body_y": 300,
  "body_bottom": 820,
  "basis": "Standardの12カラムの考え方を継承し、Companyの3事業カード（464幅・24間隔）と一致するgutter24を採用。新原稿用の割付。",
  "schemes": [
    {
      "id": "C-G01",
      "name": "1カラム",
      "spans": [
        12
      ],
      "columns": [
        {
          "x": 80,
          "width": 1440.0,
          "span": 12
        }
      ]
    },
    {
      "id": "C-G02",
      "name": "2カラム",
      "spans": [
        6,
        6
      ],
      "columns": [
        {
          "x": 80,
          "width": 708.0,
          "span": 6
        },
        {
          "x": 812.0,
          "width": 708.0,
          "span": 6
        }
      ]
    },
    {
      "id": "C-G03",
      "name": "3カラム",
      "spans": [
        4,
        4,
        4
      ],
      "columns": [
        {
          "x": 80,
          "width": 464.0,
          "span": 4
        },
        {
          "x": 568.0,
          "width": 464.0,
          "span": 4
        },
        {
          "x": 1056.0,
          "width": 464.0,
          "span": 4
        }
      ]
    },
    {
      "id": "C-G04",
      "name": "4カラム",
      "spans": [
        3,
        3,
        3,
        3
      ],
      "columns": [
        {
          "x": 80,
          "width": 342.0,
          "span": 3
        },
        {
          "x": 446.0,
          "width": 342.0,
          "span": 3
        },
        {
          "x": 812.0,
          "width": 342.0,
          "span": 3
        },
        {
          "x": 1178.0,
          "width": 342.0,
          "span": 3
        }
      ]
    },
    {
      "id": "C-G05",
      "name": "左1：右2",
      "spans": [
        4,
        8
      ],
      "columns": [
        {
          "x": 80,
          "width": 464.0,
          "span": 4
        },
        {
          "x": 568.0,
          "width": 952.0,
          "span": 8
        }
      ]
    },
    {
      "id": "C-G06",
      "name": "左2：右1",
      "spans": [
        8,
        4
      ],
      "columns": [
        {
          "x": 80,
          "width": 952.0,
          "span": 8
        },
        {
          "x": 1056.0,
          "width": 464.0,
          "span": 4
        }
      ]
    }
  ],
  "original_exceptions": {
    "profiles": {
      "lefts": [
        80,
        840
      ],
      "text_lefts": [
        300,
        1060
      ],
      "text_width": 460
    },
    "kpi_area": {
      "left": 80,
      "width": 960,
      "card_width": 228,
      "gutter": 16,
      "donut_center": [
        1305,
        525
      ]
    }
  },
  "drawing": {
    "id": "grid-schemes",
    "title": "Company 12カラムの割り付け",
    "canvas": [
      1600,
      650
    ],
    "nodes": [
      {
        "type": "rect",
        "x": 0,
        "y": 0,
        "w": 1600,
        "h": 650,
        "fill_role": "background"
      },
      {
        "type": "text",
        "x": 80,
        "y": 20,
        "w": 1440,
        "h": 36,
        "text": "C-G01 / 1カラム",
        "size": 20,
        "leading": 30.0,
        "fill_role": "muted",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 80,
        "y": 58,
        "w": 1440.0,
        "h": 46,
        "fill_role": "sub",
        "rx": 4
      },
      {
        "type": "text",
        "x": 80,
        "y": 64,
        "w": 1440.0,
        "h": 34,
        "text": "12 / 1440.0px",
        "size": 20,
        "leading": 30.0,
        "fill_role": "text",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "text",
        "x": 80,
        "y": 114,
        "w": 1440,
        "h": 36,
        "text": "C-G02 / 2カラム",
        "size": 20,
        "leading": 30.0,
        "fill_role": "muted",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 80,
        "y": 152,
        "w": 708.0,
        "h": 46,
        "fill_role": "sub",
        "rx": 4
      },
      {
        "type": "text",
        "x": 80,
        "y": 158,
        "w": 708.0,
        "h": 34,
        "text": "6 / 708.0px",
        "size": 20,
        "leading": 30.0,
        "fill_role": "text",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "rect",
        "x": 812.0,
        "y": 152,
        "w": 708.0,
        "h": 46,
        "fill_role": "sub",
        "rx": 4
      },
      {
        "type": "text",
        "x": 812.0,
        "y": 158,
        "w": 708.0,
        "h": 34,
        "text": "6 / 708.0px",
        "size": 20,
        "leading": 30.0,
        "fill_role": "text",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "text",
        "x": 80,
        "y": 208,
        "w": 1440,
        "h": 36,
        "text": "C-G03 / 3カラム",
        "size": 20,
        "leading": 30.0,
        "fill_role": "muted",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 80,
        "y": 246,
        "w": 464.0,
        "h": 46,
        "fill_role": "sub",
        "rx": 4
      },
      {
        "type": "text",
        "x": 80,
        "y": 252,
        "w": 464.0,
        "h": 34,
        "text": "4 / 464.0px",
        "size": 20,
        "leading": 30.0,
        "fill_role": "text",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "rect",
        "x": 568.0,
        "y": 246,
        "w": 464.0,
        "h": 46,
        "fill_role": "sub",
        "rx": 4
      },
      {
        "type": "text",
        "x": 568.0,
        "y": 252,
        "w": 464.0,
        "h": 34,
        "text": "4 / 464.0px",
        "size": 20,
        "leading": 30.0,
        "fill_role": "text",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "rect",
        "x": 1056.0,
        "y": 246,
        "w": 464.0,
        "h": 46,
        "fill_role": "sub",
        "rx": 4
      },
      {
        "type": "text",
        "x": 1056.0,
        "y": 252,
        "w": 464.0,
        "h": 34,
        "text": "4 / 464.0px",
        "size": 20,
        "leading": 30.0,
        "fill_role": "text",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "text",
        "x": 80,
        "y": 302,
        "w": 1440,
        "h": 36,
        "text": "C-G04 / 4カラム",
        "size": 20,
        "leading": 30.0,
        "fill_role": "muted",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 80,
        "y": 340,
        "w": 342.0,
        "h": 46,
        "fill_role": "sub",
        "rx": 4
      },
      {
        "type": "text",
        "x": 80,
        "y": 346,
        "w": 342.0,
        "h": 34,
        "text": "3 / 342.0px",
        "size": 20,
        "leading": 30.0,
        "fill_role": "text",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "rect",
        "x": 446.0,
        "y": 340,
        "w": 342.0,
        "h": 46,
        "fill_role": "sub",
        "rx": 4
      },
      {
        "type": "text",
        "x": 446.0,
        "y": 346,
        "w": 342.0,
        "h": 34,
        "text": "3 / 342.0px",
        "size": 20,
        "leading": 30.0,
        "fill_role": "text",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "rect",
        "x": 812.0,
        "y": 340,
        "w": 342.0,
        "h": 46,
        "fill_role": "sub",
        "rx": 4
      },
      {
        "type": "text",
        "x": 812.0,
        "y": 346,
        "w": 342.0,
        "h": 34,
        "text": "3 / 342.0px",
        "size": 20,
        "leading": 30.0,
        "fill_role": "text",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "rect",
        "x": 1178.0,
        "y": 340,
        "w": 342.0,
        "h": 46,
        "fill_role": "sub",
        "rx": 4
      },
      {
        "type": "text",
        "x": 1178.0,
        "y": 346,
        "w": 342.0,
        "h": 34,
        "text": "3 / 342.0px",
        "size": 20,
        "leading": 30.0,
        "fill_role": "text",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "text",
        "x": 80,
        "y": 396,
        "w": 1440,
        "h": 36,
        "text": "C-G05 / 左1：右2",
        "size": 20,
        "leading": 30.0,
        "fill_role": "muted",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 80,
        "y": 434,
        "w": 464.0,
        "h": 46,
        "fill_role": "sub",
        "rx": 4
      },
      {
        "type": "text",
        "x": 80,
        "y": 440,
        "w": 464.0,
        "h": 34,
        "text": "4 / 464.0px",
        "size": 20,
        "leading": 30.0,
        "fill_role": "text",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "rect",
        "x": 568.0,
        "y": 434,
        "w": 952.0,
        "h": 46,
        "fill_role": "sub",
        "rx": 4
      },
      {
        "type": "text",
        "x": 568.0,
        "y": 440,
        "w": 952.0,
        "h": 34,
        "text": "8 / 952.0px",
        "size": 20,
        "leading": 30.0,
        "fill_role": "text",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "text",
        "x": 80,
        "y": 490,
        "w": 1440,
        "h": 36,
        "text": "C-G06 / 左2：右1",
        "size": 20,
        "leading": 30.0,
        "fill_role": "muted",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 80,
        "y": 528,
        "w": 952.0,
        "h": 46,
        "fill_role": "sub",
        "rx": 4
      },
      {
        "type": "text",
        "x": 80,
        "y": 534,
        "w": 952.0,
        "h": 34,
        "text": "8 / 952.0px",
        "size": 20,
        "leading": 30.0,
        "fill_role": "text",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "rect",
        "x": 1056.0,
        "y": 528,
        "w": 464.0,
        "h": 46,
        "fill_role": "sub",
        "rx": 4
      },
      {
        "type": "text",
        "x": 1056.0,
        "y": 534,
        "w": 464.0,
        "h": 34,
        "text": "4 / 464.0px",
        "size": 20,
        "leading": 30.0,
        "fill_role": "text",
        "weight": 400,
        "align": "center"
      }
    ]
  }
}
```
