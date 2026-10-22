<!-- Generated from index.html#component-style. Edit index.html, not this file. -->

## Serifスタイル｜直線・細い罫線・余白

図解の共通原則を継承し、角丸・塗り・余白・影はSerifのスタイルとして定義します。Companyの丸い事業カードやシャドウを自動適用しません。

| 対象 | Serifの基準 | 観察／提案 |
| --- | --- | --- |
| 本文のまとまり | 面や影で囲まず、細い罫線と余白で区切る | 原本の事業・人物・KPI |
| 角丸 | 基本0px。写真・表・棒も直線 | 原本 |
| 罫線 | 0.5px。関係線は新規図解で1pxを初期目安 | 0.5は観察、1は提案 |
| 塗り | 説明ノードは紙色100%、文字は100% | ノード運用の提案 |
| 半透明の補助面 | 主色8%。文字・線は100%、影なし | 追加提案。背景の光とは別 |
| 丸い補助グループ | 必要な場合だけ半径4px | 追加提案。全ての部品へ適用しない |
| 影 | 原則なし。背景のぼかしを前景の影と混同しない | 原本と共通の運用 |

[見本SVG](../inline-previews/35797859ecc94fdd273a.svg)

同じ構図でSerifの基本形と、半透明の補助面を比較。右は任意の追加提案。

仕様データ

```
{
  "id": "S-STYLE",
  "inherits": "diagram-common-v1",
  "native_canvas": [
    800,
    450
  ],
  "inheritance_scope": "図解の意味・接続・重なり・編集単位を共有。Companyの寸法や角丸・影は継承しない。",
  "observed": {
    "content_radius": 0,
    "content_shadows": false,
    "hairline": 0.5,
    "bar_radius": 0,
    "photo_radius": 0,
    "number_font": "Libre Baskerville",
    "heading_font": "Noto Serif JP",
    "body_font": "Noto Sans JP"
  },
  "proposed": {
    "node": {
      "radius": 0,
      "fill_role": "background",
      "fill_opacity": 1,
      "padding": 12,
      "stroke": 0.5,
      "shadow": false
    },
    "group": {
      "radius": 0,
      "fill_role": "main",
      "fill_opacity": 0.08,
      "text_opacity": 1,
      "stroke_opacity": 1,
      "shadow": false
    },
    "density": {
      "compact": {
        "padding": 8,
        "node_gap": 12,
        "group_gap": 16
      },
      "regular": {
        "padding": 12,
        "node_gap": 16,
        "group_gap": 24
      },
      "spacious": {
        "padding": 16,
        "node_gap": 24,
        "group_gap": 32
      }
    },
    "optional_soft_group": {
      "radius": 4,
      "status": "追加提案。背景の補助面だけに限定。既存の写真・表・棒へ適用しない。"
    }
  },
  "basis": "本文は細い罫線と余白で区切る。原本のblur/noiseは背景表現であり、ノードの影ではない。",
  "drawing": {
    "id": "style-profiles",
    "title": "Serifの基本造形と補助面の提案",
    "canvas": [
      800,
      350
    ],
    "nodes": [
      {
        "type": "rect",
        "x": 0,
        "y": 0,
        "w": 800,
        "h": 350,
        "fill_role": "background"
      },
      {
        "type": "text",
        "x": 30,
        "y": 18,
        "w": 350,
        "h": 34,
        "text": "Serif / Default",
        "size": 18,
        "leading": 27.0,
        "fill_role": "heading",
        "font": "Libre Baskerville",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 30,
        "y": 68,
        "w": 350,
        "h": 190,
        "fill_role": "background",
        "rx": 0,
        "stroke_role": "line",
        "stroke-width": 0.5
      },
      {
        "type": "rect",
        "x": 42,
        "y": 86,
        "w": 326,
        "h": 66,
        "fill_role": "sub",
        "rx": 0,
        "fill-opacity": 1
      },
      {
        "type": "text",
        "x": 52,
        "y": 96,
        "w": 306,
        "h": 44,
        "text": "構図と意味は共通\n造形はSerifの規定へ",
        "size": 13,
        "leading": 20,
        "fill_role": "heading",
        "font": "Noto Serif JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 42,
        "y": 174,
        "w": 320,
        "h": 60,
        "text": "角丸 0px / 塗り 100%\n内側 12px / 間隔 16px / 影なし",
        "size": 11,
        "leading": 18,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 30,
        "y": 278,
        "w": 350,
        "h": 54,
        "text": "原本に合わせた直線的な輪郭",
        "size": 11,
        "leading": 18,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 420,
        "y": 18,
        "w": 350,
        "h": 34,
        "text": "Serif / Group tint",
        "size": 18,
        "leading": 27.0,
        "fill_role": "heading",
        "font": "Libre Baskerville",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 420,
        "y": 68,
        "w": 350,
        "h": 190,
        "fill_role": "background",
        "rx": 0,
        "stroke_role": "line",
        "stroke-width": 0.5
      },
      {
        "type": "rect",
        "x": 436,
        "y": 86,
        "w": 318,
        "h": 66,
        "fill_role": "main",
        "rx": 4,
        "fill-opacity": 0.08
      },
      {
        "type": "text",
        "x": 446,
        "y": 96,
        "w": 306,
        "h": 44,
        "text": "構図と意味は共通\n造形はSerifの規定へ",
        "size": 13,
        "leading": 20,
        "fill_role": "heading",
        "font": "Noto Serif JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 436,
        "y": 174,
        "w": 320,
        "h": 60,
        "text": "角丸 4px / 塗り 8%\n内側 16px / 間隔 24px / 影なし",
        "size": 11,
        "leading": 18,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 420,
        "y": 278,
        "w": 350,
        "h": 54,
        "text": "半透明の補助面・角丸は追加提案",
        "size": 11,
        "leading": 18,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      }
    ]
  }
}
```
