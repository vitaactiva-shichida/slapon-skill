<!-- Generated from index.html#component-table. Edit index.html, not this file. -->

## S-TABLE｜項目表・比較表・複数行セル

[見本SVG](table.svg)

原本の項目表。細い横線と明朝の項目・値を保持。

| 項目表の観察値 | 基準 |
| --- | --- |
| 領域 | x298 / y92 / 幅470、48px×6行 |
| 項目と値 | 項目x298、値x418。Noto Serif JP 14px Regular |
| 罫線 | 横線0.5px、縦線なし。塗りつぶしたヘッダーなし |

[見本SVG](../inline-previews/b4b0added602cac80311.svg)

比較表の新規提案。濃い帯や角丸・影を自動追加せず、注目列を淡い面で示す。

2行以上のセルがあれば行全体を高くします。最大行数×行送り＋上下余白で計算し、注記サイズへ縮小して詰め込みません。表を分ける場合は比較条件・単位・列幅を保ちます。

仕様データ

```
{
  "canvas": [
    800,
    450
  ],
  "observed": {
    "x": 298,
    "y": 92,
    "width": 470,
    "row_height": 48,
    "rows": 6,
    "label_x": 298,
    "value_x": 418,
    "font": "Noto Serif JP",
    "size": 14,
    "hairline": 0.5,
    "vertical_rules": false,
    "filled_header": false
  },
  "proposed": {
    "cell_padding_x": 12,
    "cell_padding_y": 12,
    "body_size": 12,
    "leading": 18,
    "min_row_height": 48,
    "highlight_columns": 1
  },
  "policy": "行高は最長セルの行数×行送り＋上下余白。数値の単位・比較条件をそろえる。分割時も同じ列幅と見出しを保つ。",
  "drawing": {
    "id": "comparison-table",
    "title": "Serifの比較表の追加見本",
    "canvas": [
      800,
      290
    ],
    "nodes": [
      {
        "type": "rect",
        "x": 0,
        "y": 0,
        "w": 800,
        "h": 290,
        "fill_role": "background"
      },
      {
        "type": "line",
        "x1": 30,
        "y1": 34,
        "x2": 210,
        "y2": 34,
        "stroke_role": "main",
        "stroke-width": 0.5
      },
      {
        "type": "text",
        "x": 42,
        "y": 48,
        "w": 156,
        "h": 35,
        "text": "比較の軸",
        "size": 13,
        "leading": 19.5,
        "fill_role": "heading",
        "font": "Noto Serif JP",
        "weight": 400
      },
      {
        "type": "line",
        "x1": 210,
        "y1": 34,
        "x2": 490,
        "y2": 34,
        "stroke_role": "main",
        "stroke-width": 0.5
      },
      {
        "type": "text",
        "x": 222,
        "y": 48,
        "w": 256,
        "h": 35,
        "text": "選択肢A",
        "size": 13,
        "leading": 19.5,
        "fill_role": "heading",
        "font": "Noto Serif JP",
        "weight": 400
      },
      {
        "type": "line",
        "x1": 490,
        "y1": 34,
        "x2": 770,
        "y2": 34,
        "stroke_role": "main",
        "stroke-width": 0.5
      },
      {
        "type": "text",
        "x": 502,
        "y": 48,
        "w": 256,
        "h": 35,
        "text": "注目する選択肢B",
        "size": 13,
        "leading": 19.5,
        "fill_role": "heading",
        "font": "Noto Serif JP",
        "weight": 400
      },
      {
        "type": "line",
        "x1": 30,
        "y1": 94,
        "x2": 210,
        "y2": 94,
        "stroke_role": "line",
        "stroke-width": 0.5
      },
      {
        "type": "text",
        "x": 42,
        "y": 107,
        "w": 156,
        "h": 36,
        "text": "説明の範囲",
        "size": 12,
        "leading": 18,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "line",
        "x1": 210,
        "y1": 94,
        "x2": 490,
        "y2": 94,
        "stroke_role": "line",
        "stroke-width": 0.5
      },
      {
        "type": "text",
        "x": 222,
        "y": 107,
        "w": 256,
        "h": 36,
        "text": "内容を整理",
        "size": 12,
        "leading": 18,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 490,
        "y": 94,
        "w": 280,
        "h": 55,
        "fill_role": "sub"
      },
      {
        "type": "line",
        "x1": 490,
        "y1": 94,
        "x2": 770,
        "y2": 94,
        "stroke_role": "line",
        "stroke-width": 0.5
      },
      {
        "type": "text",
        "x": 502,
        "y": 107,
        "w": 256,
        "h": 36,
        "text": "整理から実行まで",
        "size": 12,
        "leading": 18,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "line",
        "x1": 30,
        "y1": 149,
        "x2": 210,
        "y2": 149,
        "stroke_role": "line",
        "stroke-width": 0.5
      },
      {
        "type": "text",
        "x": 42,
        "y": 162,
        "w": 156,
        "h": 36,
        "text": "確認の方法",
        "size": 12,
        "leading": 18,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "line",
        "x1": 210,
        "y1": 149,
        "x2": 490,
        "y2": 149,
        "stroke_role": "line",
        "stroke-width": 0.5
      },
      {
        "type": "text",
        "x": 222,
        "y": 162,
        "w": 256,
        "h": 36,
        "text": "文章で確認",
        "size": 12,
        "leading": 18,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 490,
        "y": 149,
        "w": 280,
        "h": 55,
        "fill_role": "sub"
      },
      {
        "type": "line",
        "x1": 490,
        "y1": 149,
        "x2": 770,
        "y2": 149,
        "stroke_role": "line",
        "stroke-width": 0.5
      },
      {
        "type": "text",
        "x": 502,
        "y": 162,
        "w": 256,
        "h": 36,
        "text": "見本と数値を照合",
        "size": 12,
        "leading": 18,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "line",
        "x1": 30,
        "y1": 204,
        "x2": 210,
        "y2": 204,
        "stroke_role": "line",
        "stroke-width": 0.5
      },
      {
        "type": "text",
        "x": 42,
        "y": 217,
        "w": 156,
        "h": 36,
        "text": "編集の単位",
        "size": 12,
        "leading": 18,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "line",
        "x1": 210,
        "y1": 204,
        "x2": 490,
        "y2": 204,
        "stroke_role": "line",
        "stroke-width": 0.5
      },
      {
        "type": "text",
        "x": 222,
        "y": 217,
        "w": 256,
        "h": 36,
        "text": "要素ごとに保持",
        "size": 12,
        "leading": 18,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 490,
        "y": 204,
        "w": 280,
        "h": 55,
        "fill_role": "sub"
      },
      {
        "type": "line",
        "x1": 490,
        "y1": 204,
        "x2": 770,
        "y2": 204,
        "stroke_role": "line",
        "stroke-width": 0.5
      },
      {
        "type": "text",
        "x": 502,
        "y": 217,
        "w": 256,
        "h": 36,
        "text": "文章は段落として保持",
        "size": 12,
        "leading": 18,
        "fill_role": "text",
        "font": "Noto Sans JP",
        "weight": 400
      },
      {
        "type": "line",
        "x1": 30,
        "y1": 259,
        "x2": 770,
        "y2": 259,
        "stroke_role": "line",
        "stroke-width": 0.5
      }
    ]
  }
}
```
