<!-- Generated from index.html#component-spacing. Edit index.html, not this file. -->

## 余白密度｜Compact・Regular・Spacious

通常の図解は内側12px・部品間16px・グループ間24pxを初期値にします。密度を変えても文字サイズをばらばらにせず、同じ階層の間隔をそろえます。

[見本SVG](../inline-previews/733337dd03d7bc0c910f.svg)

同じ12pxの文字で比較。最も狭い設定へ文章を押し込まず、必要な高さを確保する。

| 対象 | 初期値 | 例外 |
| --- | --- | --- |
| 図解ノード内部 | 12px | 短いラベルのCompact 8px／Spacious 16px |
| 同一グループ内 | 16px | Compact 12px／Spacious 24px |
| 別グループ間 | 24px | Compact 16px／Spacious 32px |
| 線とラベル | 4px以上 | 文字の輪郭から測る。 |
| 写真・事業3列の間 | 22px | 原本の固有値。図解の間隔へ一律適用しない。 |

仕様データ

```
{
  "canvas": [
    800,
    450
  ],
  "inherits": "diagram-common-v1",
  "profiles": {
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
  "clearance": {
    "text_to_edge_min": 8,
    "label_to_connector": 4
  },
  "status": "新規図解の提案。原本の部品間22px・表の行高48pxとは役割を分ける。",
  "drawing": {
    "id": "spacing-density",
    "title": "Serifの余白密度",
    "canvas": [
      800,
      285
    ],
    "nodes": [
      {
        "type": "rect",
        "x": 0,
        "y": 0,
        "w": 800,
        "h": 285,
        "fill_role": "background"
      },
      {
        "type": "text",
        "x": 20,
        "y": 14,
        "w": 240,
        "h": 28,
        "text": "Compact",
        "size": 15,
        "leading": 22.5,
        "fill_role": "heading",
        "font": "Libre Baskerville",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 20,
        "y": 60,
        "w": 240,
        "h": 142,
        "fill_role": "background",
        "stroke_role": "line",
        "stroke-width": 0.5
      },
      {
        "type": "rect",
        "x": 28,
        "y": 68,
        "w": 224,
        "h": 32,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 33,
        "y": 72,
        "w": 194,
        "h": 22,
        "text": "共通の文字サイズ12px",
        "size": 12,
        "leading": 18.0,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 28,
        "y": 112,
        "w": 224,
        "h": 32,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 33,
        "y": 116,
        "w": 194,
        "h": 22,
        "text": "余白の密度だけを変える",
        "size": 12,
        "leading": 18.0,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 20,
        "y": 223,
        "w": 240,
        "h": 40,
        "text": "内側8px / 間隔12px",
        "size": 11,
        "leading": 16.5,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 280,
        "y": 14,
        "w": 240,
        "h": 28,
        "text": "Regular",
        "size": 15,
        "leading": 22.5,
        "fill_role": "heading",
        "font": "Libre Baskerville",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 280,
        "y": 60,
        "w": 240,
        "h": 142,
        "fill_role": "background",
        "stroke_role": "line",
        "stroke-width": 0.5
      },
      {
        "type": "rect",
        "x": 292,
        "y": 72,
        "w": 216,
        "h": 32,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 297,
        "y": 76,
        "w": 186,
        "h": 22,
        "text": "共通の文字サイズ12px",
        "size": 12,
        "leading": 18.0,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 292,
        "y": 120,
        "w": 216,
        "h": 32,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 297,
        "y": 124,
        "w": 186,
        "h": 22,
        "text": "余白の密度だけを変える",
        "size": 12,
        "leading": 18.0,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 280,
        "y": 223,
        "w": 240,
        "h": 40,
        "text": "内側12px / 間隔16px",
        "size": 11,
        "leading": 16.5,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 540,
        "y": 14,
        "w": 240,
        "h": 28,
        "text": "Spacious",
        "size": 15,
        "leading": 22.5,
        "fill_role": "heading",
        "font": "Libre Baskerville",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 540,
        "y": 60,
        "w": 240,
        "h": 142,
        "fill_role": "background",
        "stroke_role": "line",
        "stroke-width": 0.5
      },
      {
        "type": "rect",
        "x": 556,
        "y": 76,
        "w": 208,
        "h": 32,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 561,
        "y": 80,
        "w": 178,
        "h": 22,
        "text": "共通の文字サイズ12px",
        "size": 12,
        "leading": 18.0,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 556,
        "y": 132,
        "w": 208,
        "h": 32,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 561,
        "y": 136,
        "w": 178,
        "h": 22,
        "text": "余白の密度だけを変える",
        "size": 12,
        "leading": 18.0,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 540,
        "y": 223,
        "w": 240,
        "h": 40,
        "text": "内側16px / 間隔24px",
        "size": 11,
        "leading": 16.5,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      }
    ]
  }
}
```
