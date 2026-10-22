<!-- Generated from index.html#component-primitives. Edit index.html, not this file. -->

## C-P01–P06｜説明・プロフィール・工程・接続

[見本SVG](card.svg)

C-P01：影はカード外側、内側28px。原本の事業カード。

[見本SVG](profile.svg)

C-P02：写真・氏名・タグ・紹介文。紹介文は17px・行送り28px。

[見本SVG](process.svg)

C-P03：300×64pxの工程ピル、縦ピッチ94px、説明x428。工程数は可変。

文章が長い場合は行高や段の高さを増やし、次の行や部品を送ります。写真は比率を保ち、氏名・専門タグ・説明文の編集単位を分けます。数値と単位は書式を分けても同じ基準線にそろえます。矢印は順序や移動を意味するときに使い、単なる並列を矢印でつなぎません。

仕様データ

```
{
  "components": [
    {
      "id": "C-P01",
      "name": "説明カード",
      "style": "container or node",
      "variable": "見出し・説明文・要素数"
    },
    {
      "id": "C-P02",
      "name": "プロフィール",
      "source": "members",
      "anchors": {
        "photo_x": 80,
        "text_x": 300,
        "rule_y": 277,
        "text_width": 460
      },
      "variable": "人数・写真・紹介文"
    },
    {
      "id": "C-P03",
      "name": "工程",
      "source": "selection",
      "pill": [
        80,
        220,
        300,
        64
      ],
      "row_pitch": 94,
      "text_x": 428,
      "text_size": 17,
      "leading": 28,
      "variable": "工程数・順序・説明"
    },
    {
      "id": "C-P04",
      "name": "KPI",
      "source": "culture",
      "variable": "数値・指標・単位・比較条件"
    },
    {
      "id": "C-P05",
      "name": "接続",
      "stroke_width": 2,
      "arrowhead": 8,
      "label_clearance": 8,
      "variable": "接続先・方向"
    },
    {
      "id": "C-P06",
      "name": "写真・図版",
      "fit": "比率保持。領域内でトリミング",
      "variable": "素材・被写体の位置"
    }
  ],
  "fixed": "同じ階層の文字役割・角丸・塗り・間隔をそろえる",
  "flexible": "数・並び・本文量は原稿から判断。元作例を人数や工程数の制約にしない。"
}
```
