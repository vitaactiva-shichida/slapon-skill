<!-- Generated from index.html#component-table. Edit index.html, not this file. -->

## C-TABLE｜項目表・比較表・行の増減

{{component.table}}

会社概要の項目表。原本の列位置・行送りを保持。

| 原本の項目表 | 参照値 |
| --- | --- |
| 領域 | x80 / y250 / w1440、82px×6行 |
| 項目と値 | 項目x80・23px Bold、値x288・25px Regular |
| 区切り | 横線2px、縦罫線なし、塗りつぶした見出し行なし |

比較表を新しく組む場合は、比較軸・列幅・数値の単位をそろえ、注目列だけを強調します。Companyの項目表へStandardの塗りつぶしヘッダーを自動で付ける指定ではありません。

{{detail.comparison-table}}

Company配色で組む比較表の追加見本。文言は架空の配置見本。

2行以上のセルは行全体の高さを増やします。最長セルを基準に、行高＝最大行数×行送り＋上下余白で計算。ページを分けるときは見出しを繰り返し、同じ列幅・単位を保ちます。

仕様データ

```
{
  "id": "C-TABLE",
  "observed": {
    "key_value": {
      "x": 80,
      "y": 250,
      "width": 1440,
      "row_height": 82,
      "rows": 6,
      "label_x": 80,
      "value_x": 288,
      "label_size": 23,
      "value_size": 25,
      "separator_width": 2,
      "vertical_rules": false,
      "filled_header": false
    }
  },
  "proposed": {
    "comparison": {
      "padding_x": 24,
      "padding_y": 24,
      "cell_size": 22,
      "leading": 32,
      "min_row_height": 80,
      "highlight_columns": 1,
      "repeat_header_on_split": true
    }
  },
  "policy": "行高は最大セルの行数×行送り＋上下余白で決める。数値列は右寄せ、単位と比較条件をそろえる。結合セルや小文字化で情報を押し込まない。",
  "drawing": {
    "id": "comparison-table",
    "title": "比較表の部品見本",
    "canvas": [
      1600,
      460
    ],
    "nodes": [
      {
        "type": "rect",
        "x": 0,
        "y": 0,
        "w": 1600,
        "h": 460,
        "fill_role": "background"
      },
      {
        "type": "rect",
        "x": 60,
        "y": 44,
        "w": 400,
        "h": 70,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 84,
        "y": 58,
        "w": 352,
        "h": 44,
        "text": "比較の軸",
        "size": 24,
        "leading": 36.0,
        "fill_role": "inkSurface",
        "weight": 700
      },
      {
        "type": "rect",
        "x": 460,
        "y": 44,
        "w": 540,
        "h": 70,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 484,
        "y": 58,
        "w": 492,
        "h": 44,
        "text": "選択肢A",
        "size": 24,
        "leading": 36.0,
        "fill_role": "inkSurface",
        "weight": 700
      },
      {
        "type": "rect",
        "x": 1000,
        "y": 44,
        "w": 540,
        "h": 70,
        "fill_role": "main"
      },
      {
        "type": "text",
        "x": 1024,
        "y": 58,
        "w": 492,
        "h": 44,
        "text": "注目する選択肢B",
        "size": 24,
        "leading": 36.0,
        "fill_role": "onmain",
        "weight": 700
      },
      {
        "type": "rect",
        "x": 60,
        "y": 114,
        "w": 400,
        "h": 94,
        "fill_role": "background"
      },
      {
        "type": "text",
        "x": 84,
        "y": 138,
        "w": 352,
        "h": 66,
        "text": "対応範囲",
        "size": 22,
        "leading": 32,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "line",
        "x1": 60,
        "y1": 208,
        "x2": 460,
        "y2": 208,
        "stroke_role": "line",
        "stroke-width": 1
      },
      {
        "type": "rect",
        "x": 460,
        "y": 114,
        "w": 540,
        "h": 94,
        "fill_role": "background"
      },
      {
        "type": "text",
        "x": 484,
        "y": 138,
        "w": 492,
        "h": 66,
        "text": "対象を整理",
        "size": 22,
        "leading": 32,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "line",
        "x1": 460,
        "y1": 208,
        "x2": 1000,
        "y2": 208,
        "stroke_role": "line",
        "stroke-width": 1
      },
      {
        "type": "rect",
        "x": 1000,
        "y": 114,
        "w": 540,
        "h": 94,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 1024,
        "y": 138,
        "w": 492,
        "h": 66,
        "text": "整理から実行まで",
        "size": 22,
        "leading": 32,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "line",
        "x1": 1000,
        "y1": 208,
        "x2": 1540,
        "y2": 208,
        "stroke_role": "line",
        "stroke-width": 1
      },
      {
        "type": "rect",
        "x": 60,
        "y": 208,
        "w": 400,
        "h": 94,
        "fill_role": "background"
      },
      {
        "type": "text",
        "x": 84,
        "y": 232,
        "w": 352,
        "h": 66,
        "text": "進め方",
        "size": 22,
        "leading": 32,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "line",
        "x1": 60,
        "y1": 302,
        "x2": 460,
        "y2": 302,
        "stroke_role": "line",
        "stroke-width": 1
      },
      {
        "type": "rect",
        "x": 460,
        "y": 208,
        "w": 540,
        "h": 94,
        "fill_role": "background"
      },
      {
        "type": "text",
        "x": 484,
        "y": 232,
        "w": 492,
        "h": 66,
        "text": "個別に対応",
        "size": 22,
        "leading": 32,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "line",
        "x1": 460,
        "y1": 302,
        "x2": 1000,
        "y2": 302,
        "stroke_role": "line",
        "stroke-width": 1
      },
      {
        "type": "rect",
        "x": 1000,
        "y": 208,
        "w": 540,
        "h": 94,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 1024,
        "y": 232,
        "w": 492,
        "h": 66,
        "text": "複数部品を組み合わせる",
        "size": 22,
        "leading": 32,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "line",
        "x1": 1000,
        "y1": 302,
        "x2": 1540,
        "y2": 302,
        "stroke_role": "line",
        "stroke-width": 1
      },
      {
        "type": "rect",
        "x": 60,
        "y": 302,
        "w": 400,
        "h": 94,
        "fill_role": "background"
      },
      {
        "type": "text",
        "x": 84,
        "y": 326,
        "w": 352,
        "h": 66,
        "text": "確認方法",
        "size": 22,
        "leading": 32,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "line",
        "x1": 60,
        "y1": 396,
        "x2": 460,
        "y2": 396,
        "stroke_role": "line",
        "stroke-width": 1
      },
      {
        "type": "rect",
        "x": 460,
        "y": 302,
        "w": 540,
        "h": 94,
        "fill_role": "background"
      },
      {
        "type": "text",
        "x": 484,
        "y": 326,
        "w": 492,
        "h": 66,
        "text": "文章で確認",
        "size": 22,
        "leading": 32,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "line",
        "x1": 460,
        "y1": 396,
        "x2": 1000,
        "y2": 396,
        "stroke_role": "line",
        "stroke-width": 1
      },
      {
        "type": "rect",
        "x": 1000,
        "y": 302,
        "w": 540,
        "h": 94,
        "fill_role": "sub"
      },
      {
        "type": "text",
        "x": 1024,
        "y": 326,
        "w": 492,
        "h": 66,
        "text": "見本と数値を照合",
        "size": 22,
        "leading": 32,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "line",
        "x1": 1000,
        "y1": 396,
        "x2": 1540,
        "y2": 396,
        "stroke_role": "line",
        "stroke-width": 1
      }
    ]
  }
}
```
