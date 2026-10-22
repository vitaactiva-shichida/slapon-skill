<!-- Generated from index.html#component-layers. Edit index.html, not this file. -->

## 重なりと半透明｜文字・線を薄くしない

半透明を使う場合は補助面のfill-opacityだけへ設定します。Serifの背景PNGの光と、図解の透明度を混同しません。手前の説明ノードは紙色100%で背面を隠します。

[見本SVG](../inline-previews/be7845e644c1031709a5.svg)

8%を2枚重ねた合成濃度は1−0.92²＝15.36%。重なりに分類の意味を与える見本ではない。

原本の棒グラフには棒ごとの透明度38・48・58・68・78・100%があります。文字を含むグループ全体の透明度ではありません。この固有の濃淡を、全図解の既定値にしません。

仕様データ

```
{
  "canvas": [
    800,
    450
  ],
  "inherits": "diagram-common-v1",
  "group_alpha": 0.08,
  "node_alpha": 1,
  "text_alpha": 1,
  "line_alpha": 1,
  "combined_alpha": 0.1536,
  "drawing": {
    "id": "layers-alpha",
    "title": "半透明の補助面と不透明な説明ノード",
    "canvas": [
      800,
      300
    ],
    "nodes": [
      {
        "type": "rect",
        "x": 0,
        "y": 0,
        "w": 800,
        "h": 300,
        "fill_role": "background"
      },
      {
        "type": "rect",
        "x": 40,
        "y": 45,
        "w": 720,
        "h": 180,
        "fill_role": "main",
        "fill-opacity": 0.08
      },
      {
        "type": "rect",
        "x": 400,
        "y": 45,
        "w": 360,
        "h": 180,
        "fill_role": "main",
        "fill-opacity": 0.08
      },
      {
        "type": "line",
        "x1": 260,
        "y1": 130,
        "x2": 540,
        "y2": 130,
        "stroke_role": "main",
        "stroke-width": 1
      },
      {
        "type": "rect",
        "x": 80,
        "y": 80,
        "w": 220,
        "h": 100,
        "fill_role": "background",
        "stroke_role": "line",
        "stroke-width": 0.5
      },
      {
        "type": "rect",
        "x": 500,
        "y": 80,
        "w": 220,
        "h": 100,
        "fill_role": "background",
        "stroke_role": "line",
        "stroke-width": 0.5
      },
      {
        "type": "text",
        "x": 92,
        "y": 101,
        "w": 196,
        "h": 60,
        "text": "手前の面は100%\n背面の線を隠す",
        "size": 13,
        "leading": 20,
        "fill_role": "heading",
        "font": "Noto Serif JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 512,
        "y": 101,
        "w": 196,
        "h": 60,
        "text": "塗りだけ半透明\n文字と線は100%",
        "size": 13,
        "leading": 20,
        "fill_role": "heading",
        "font": "Noto Serif JP",
        "weight": 400
      },
      {
        "type": "text",
        "x": 40,
        "y": 246,
        "w": 720,
        "h": 40,
        "text": "左：8% 1枚 ／ 右：8%を2枚重ね、合成15.36%相当",
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
