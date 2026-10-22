<!-- Generated from index.html#component-layers. Edit index.html, not this file. -->

## 重なりと半透明｜塗り・文字・輪郭を分離する

テンプレートで半透明の塗りを使う場合も、文字・接続線・輪郭の透明度は独立させます。Companyの既存の事業カードやKPIは不透明100%。下の12%は補助グループ面に限定する追加提案です。

[見本SVG](../inline-previews/e53f015bef27d0865c80.svg)

左側は12%の補助面1枚、右側は12%を2枚重ねた22.56%相当の面。手前のノードは100%で背面を隠す。構図やノード数は固定しない。

同じ塗りを重ねると見かけの濃度は変わります。12%を同じ背景上で2枚重ねる例では1−(1−0.12)²＝22.56%です。交差領域が別の分類に見えないか確認します。曲線背景の40%・10%はその素材固有の値であり、図解ノードの透明度へ流用しません。

仕様データ

```
{
  "inherits": "diagram-common-v1",
  "group_fill_opacity": 0.12,
  "node_fill_opacity": 1,
  "text_opacity": 1,
  "stroke_opacity": 1,
  "layer_order": [
    "補助面",
    "接続線",
    "不透明ノード",
    "アイコン",
    "文字"
  ],
  "white_node_policy": "Companyのカード面backgroundを100%で塗る。背面の輪郭を透かさない。",
  "drawing": {
    "id": "layers-alpha",
    "title": "半透明のグループ面と不透明な説明ノード",
    "canvas": [
      1600,
      600
    ],
    "nodes": [
      {
        "type": "rect",
        "x": 0,
        "y": 0,
        "w": 1600,
        "h": 600,
        "fill_role": "background"
      },
      {
        "type": "rect",
        "x": 80,
        "y": 90,
        "w": 1440,
        "h": 350,
        "fill_role": "main",
        "rx": 12,
        "fill-opacity": 0.12
      },
      {
        "type": "rect",
        "x": 760,
        "y": 90,
        "w": 760,
        "h": 350,
        "fill_role": "main",
        "rx": 12,
        "fill-opacity": 0.12
      },
      {
        "type": "rect",
        "x": 160,
        "y": 150,
        "w": 480,
        "h": 210,
        "fill_role": "background",
        "rx": 12,
        "stroke_role": "line",
        "stroke-width": 2
      },
      {
        "type": "line",
        "x1": 640,
        "y1": 255,
        "x2": 960,
        "y2": 255,
        "stroke_role": "main",
        "stroke-width": 2
      },
      {
        "type": "rect",
        "x": 960,
        "y": 150,
        "w": 480,
        "h": 210,
        "fill_role": "background",
        "rx": 12,
        "stroke_role": "line",
        "stroke-width": 2
      },
      {
        "type": "text",
        "x": 192,
        "y": 180,
        "w": 416,
        "h": 100,
        "text": "手前のノードは100%\n背面の線を隠す",
        "size": 28,
        "leading": 42,
        "fill_role": "text",
        "weight": 700
      },
      {
        "type": "text",
        "x": 992,
        "y": 180,
        "w": 416,
        "h": 100,
        "text": "文字・輪郭は100%\n塗りのalphaと分離",
        "size": 28,
        "leading": 42,
        "fill_role": "text",
        "weight": 700
      },
      {
        "type": "text",
        "x": 80,
        "y": 480,
        "w": 1440,
        "h": 82,
        "text": "補助面12% → 接続線 → 不透明ノード → アイコン・文字",
        "size": 26,
        "leading": 39.0,
        "fill_role": "text",
        "weight": 400
      }
    ]
  },
  "overlap_example": {
    "first_alpha": 0.12,
    "second_alpha": 0.12,
    "combined_alpha": 0.2256,
    "meaning": "透明度の確認用。分類の意味を与えない。"
  }
}
```
