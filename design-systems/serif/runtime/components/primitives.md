<!-- Generated from index.html#component-primitives. Edit index.html, not this file. -->

## S-P01–P04｜説明・人物・工程・接続

[見本SVG](business.svg)

説明のまとまり：短い罫線と見出し。カード面や影はなし。

[見本SVG](profile.svg)

人物：写真224×135、氏名・タグ・説明文を分ける。

[見本SVG](process.svg)

工程：番号・名称・説明を同じ行へ。ピルへ置き換えない。

人物は写真・氏名・タグ・説明を独立した編集単位にし、紹介文は段落として保持します。写真は比率を保ってトリミングし、引き伸ばしません。工程は説明の行数から高さを決め、原本の6工程に固定しません。関連は線、順序や移動は矢印として表現します。

仕様データ

```
{
  "canvas": [
    800,
    450
  ],
  "items": [
    {
      "id": "S-P01",
      "name": "説明のまとまり",
      "radius": 0,
      "shadow": false,
      "rule": 0.5
    },
    {
      "id": "S-P02",
      "name": "プロフィール",
      "photo": [
        42,
        113,
        224,
        135
      ],
      "person_name": {
        "size": 21,
        "font": "Noto Serif JP"
      },
      "tag_size": 8,
      "body_size": 10,
      "body_leading": 15.5
    },
    {
      "id": "S-P03",
      "name": "工程",
      "x": 42,
      "y": 124,
      "width": 716,
      "pitch": 46,
      "number": {
        "x": 42,
        "size": 16,
        "font": "Libre Baskerville"
      },
      "label": {
        "x": 95,
        "size": 13,
        "font": "Noto Serif JP"
      },
      "description": {
        "x": 263,
        "size": 10,
        "leading": 15.5
      }
    },
    {
      "id": "S-P04",
      "name": "接続",
      "stroke": 1,
      "arrowhead": 4,
      "label_clearance": 4
    }
  ],
  "variable": "人数・事業数・工程数・文章は原稿に応じて変更。"
}
```
