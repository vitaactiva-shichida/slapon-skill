<!-- Generated from index.html#component-grid. Edit index.html, not this file. -->

## S-G01–G06｜余白・カラム・固有の割付

通常の横並びは左右42px、本文幅716px、部品間22pxが原本の出発点です。12ユニットの幅は39.5px。Companyの1440px幅や24px間隔をそのまま転記しません。

[見本SVG](../inline-previews/3b9e44ad5d0378aa8dbd.svg)

新原稿用の割付。背景の光の位置と、内容のカラム数は別に選ぶ。

| 構成 | 列のx / 幅 |
| --- | --- |
| S-G01 1カラム | x42 / w716.0 |
| S-G02 2カラム | x42 / w347.0 ／ x411.0 / w347.0 |
| S-G03 3カラム | x42 / w224.0 ／ x288.0 / w224.0 ／ x534.0 / w224.0 |
| S-G04 4カラム | x42 / w162.5 ／ x226.5 / w162.5 ／ x411.0 / w162.5 ／ x595.5 / w162.5 |
| S-G05 左1：右2 | x42 / w224.0 ／ x288.0 / w470.0 |
| S-G06 左2：右1 | x42 / w470.0 ／ x534.0 / w224.0 |

会社概要の左見出しx36と表x298・幅470、KPIの110px×4列・16px間隔は原本固有の配置です。既存作例を新しい12ユニットへ正規化しません。

仕様データ

```
{
  "canvas": [
    800,
    450
  ],
  "left": 42,
  "right": 758,
  "width": 716,
  "units": 12,
  "gutter": 22,
  "unit_width": 39.5,
  "schemes": [
    {
      "id": "S-G01",
      "name": "1カラム",
      "spans": [
        12
      ],
      "columns": [
        {
          "x": 42,
          "width": 716.0,
          "span": 12
        }
      ]
    },
    {
      "id": "S-G02",
      "name": "2カラム",
      "spans": [
        6,
        6
      ],
      "columns": [
        {
          "x": 42,
          "width": 347.0,
          "span": 6
        },
        {
          "x": 411.0,
          "width": 347.0,
          "span": 6
        }
      ]
    },
    {
      "id": "S-G03",
      "name": "3カラム",
      "spans": [
        4,
        4,
        4
      ],
      "columns": [
        {
          "x": 42,
          "width": 224.0,
          "span": 4
        },
        {
          "x": 288.0,
          "width": 224.0,
          "span": 4
        },
        {
          "x": 534.0,
          "width": 224.0,
          "span": 4
        }
      ]
    },
    {
      "id": "S-G04",
      "name": "4カラム",
      "spans": [
        3,
        3,
        3,
        3
      ],
      "columns": [
        {
          "x": 42,
          "width": 162.5,
          "span": 3
        },
        {
          "x": 226.5,
          "width": 162.5,
          "span": 3
        },
        {
          "x": 411.0,
          "width": 162.5,
          "span": 3
        },
        {
          "x": 595.5,
          "width": 162.5,
          "span": 3
        }
      ]
    },
    {
      "id": "S-G05",
      "name": "左1：右2",
      "spans": [
        4,
        8
      ],
      "columns": [
        {
          "x": 42,
          "width": 224.0,
          "span": 4
        },
        {
          "x": 288.0,
          "width": 470.0,
          "span": 8
        }
      ]
    },
    {
      "id": "S-G06",
      "name": "左2：右1",
      "spans": [
        8,
        4
      ],
      "columns": [
        {
          "x": 42,
          "width": 470.0,
          "span": 8
        },
        {
          "x": 534.0,
          "width": 224.0,
          "span": 4
        }
      ]
    }
  ],
  "basis": "原本の人物・事業3列はx42/288/534、幅224、間隔22。これに一致する12ユニットを新原稿の割付に展開。",
  "exceptions": {
    "overview": {
      "heading_x": 36,
      "table_x": 298,
      "table_width": 470,
      "right": 768
    },
    "kpi": {
      "lefts": [
        42,
        168,
        294,
        420
      ],
      "width": 110,
      "gutter": 16,
      "donut_center": [
        655,
        250
      ]
    }
  },
  "drawing": {
    "id": "grid-schemes",
    "title": "Serifの12ユニット割付",
    "canvas": [
      800,
      400
    ],
    "nodes": [
      {
        "type": "rect",
        "x": 0,
        "y": 0,
        "w": 800,
        "h": 400,
        "fill_role": "background"
      },
      {
        "type": "text",
        "x": 42,
        "y": 17,
        "w": 716,
        "h": 22,
        "text": "S-G01 / 1カラム",
        "size": 10,
        "leading": 15.0,
        "fill_role": "muted",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 42,
        "y": 40,
        "w": 716.0,
        "h": 26,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 42,
        "y": 44,
        "w": 716.0,
        "h": 21,
        "text": "12 / 716.0px",
        "size": 10,
        "leading": 15.0,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "text",
        "x": 42,
        "y": 75,
        "w": 716,
        "h": 22,
        "text": "S-G02 / 2カラム",
        "size": 10,
        "leading": 15.0,
        "fill_role": "muted",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 42,
        "y": 98,
        "w": 347.0,
        "h": 26,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 42,
        "y": 102,
        "w": 347.0,
        "h": 21,
        "text": "6 / 347.0px",
        "size": 10,
        "leading": 15.0,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "rect",
        "x": 411.0,
        "y": 98,
        "w": 347.0,
        "h": 26,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 411.0,
        "y": 102,
        "w": 347.0,
        "h": 21,
        "text": "6 / 347.0px",
        "size": 10,
        "leading": 15.0,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "text",
        "x": 42,
        "y": 133,
        "w": 716,
        "h": 22,
        "text": "S-G03 / 3カラム",
        "size": 10,
        "leading": 15.0,
        "fill_role": "muted",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 42,
        "y": 156,
        "w": 224.0,
        "h": 26,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 42,
        "y": 160,
        "w": 224.0,
        "h": 21,
        "text": "4 / 224.0px",
        "size": 10,
        "leading": 15.0,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "rect",
        "x": 288.0,
        "y": 156,
        "w": 224.0,
        "h": 26,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 288.0,
        "y": 160,
        "w": 224.0,
        "h": 21,
        "text": "4 / 224.0px",
        "size": 10,
        "leading": 15.0,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "rect",
        "x": 534.0,
        "y": 156,
        "w": 224.0,
        "h": 26,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 534.0,
        "y": 160,
        "w": 224.0,
        "h": 21,
        "text": "4 / 224.0px",
        "size": 10,
        "leading": 15.0,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "text",
        "x": 42,
        "y": 191,
        "w": 716,
        "h": 22,
        "text": "S-G04 / 4カラム",
        "size": 10,
        "leading": 15.0,
        "fill_role": "muted",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 42,
        "y": 214,
        "w": 162.5,
        "h": 26,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 42,
        "y": 218,
        "w": 162.5,
        "h": 21,
        "text": "3 / 162.5px",
        "size": 10,
        "leading": 15.0,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "rect",
        "x": 226.5,
        "y": 214,
        "w": 162.5,
        "h": 26,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 226.5,
        "y": 218,
        "w": 162.5,
        "h": 21,
        "text": "3 / 162.5px",
        "size": 10,
        "leading": 15.0,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "rect",
        "x": 411.0,
        "y": 214,
        "w": 162.5,
        "h": 26,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 411.0,
        "y": 218,
        "w": 162.5,
        "h": 21,
        "text": "3 / 162.5px",
        "size": 10,
        "leading": 15.0,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "rect",
        "x": 595.5,
        "y": 214,
        "w": 162.5,
        "h": 26,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 595.5,
        "y": 218,
        "w": 162.5,
        "h": 21,
        "text": "3 / 162.5px",
        "size": 10,
        "leading": 15.0,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "text",
        "x": 42,
        "y": 249,
        "w": 716,
        "h": 22,
        "text": "S-G05 / 左1：右2",
        "size": 10,
        "leading": 15.0,
        "fill_role": "muted",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 42,
        "y": 272,
        "w": 224.0,
        "h": 26,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 42,
        "y": 276,
        "w": 224.0,
        "h": 21,
        "text": "4 / 224.0px",
        "size": 10,
        "leading": 15.0,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "rect",
        "x": 288.0,
        "y": 272,
        "w": 470.0,
        "h": 26,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 288.0,
        "y": 276,
        "w": 470.0,
        "h": 21,
        "text": "8 / 470.0px",
        "size": 10,
        "leading": 15.0,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "text",
        "x": 42,
        "y": 307,
        "w": 716,
        "h": 22,
        "text": "S-G06 / 左2：右1",
        "size": 10,
        "leading": 15.0,
        "fill_role": "muted",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 42,
        "y": 330,
        "w": 470.0,
        "h": 26,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 42,
        "y": 334,
        "w": 470.0,
        "h": 21,
        "text": "8 / 470.0px",
        "size": 10,
        "leading": 15.0,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400,
        "align": "center"
      },
      {
        "type": "rect",
        "x": 534.0,
        "y": 330,
        "w": 224.0,
        "h": 26,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 534.0,
        "y": 334,
        "w": 224.0,
        "h": 21,
        "text": "4 / 224.0px",
        "size": 10,
        "leading": 15.0,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400,
        "align": "center"
      }
    ]
  }
}
```
