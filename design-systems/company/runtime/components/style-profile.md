<!-- Generated from index.html#component-style. Edit index.html, not this file. -->

## Companyスタイル｜角丸・半透明・余白・シャドウ

共通ルールと、テンプレートの造形値を分離します。CompanyはStandardの角丸4px・影なしを一律適用せず、既存の事業カード・KPI・ピルの実物から部品ごとの値を定義します。

| 部品 | 角丸 | 塗り | 内側余白 | 影 | 根拠 |
| --- | --- | --- | --- | --- | --- |
| 新規図解ノード | 12px | sub・100% | 24px | なし | Companyへ展開する初期提案 |
| 事業カード・大きなまとまり | 12px | background・100% | 28px | 下4 / σ10 / 黒15% | 事業紹介の実配置 |
| 引用の白パネル | 12px | background・100% | 40pxを目安 | 下4 / σ7.5 / 黒20% | 社員の声の実物。余白は新原稿で再配分 |
| KPIカード | 14px | 役割色・100% | 20px | なし | データページの実配置 |
| 工程ピル | 32px（高さ64） | 系列色・100% | ラベルを中央配置 | なし | 選考プロセスの実配置 |
| 補助グループ面 | 12px | main・12% | 24px | なし | 任意の新規表現。背景ごとの合成色を確認 |

[見本SVG](detail-style-profiles.svg)

同じCompany配色で構図を共通にし、スタイルを比較。中央は28pxのカード余白。右端は半透明・狭い余白の提案で、Company全体の既定値ではない。

影は情報をひとまとまりにする外側の面に限定します。すべてのノード・矢印・グラフへ追加しません。密度を変更しても本文サイズはそろえ、文字を小さくして狭い余白へ押し込みません。影のぼかしはSVGのstdDeviation（σ）で記録し、CSSのblur半径と同じ数値と扱いません。

仕様データ

```
{
  "inherits": "diagram-common-v1",
  "unit": "reference_px",
  "standard_reference": {
    "source": "slapon-standard/index.html#component-diagram",
    "radius": 4,
    "fill_opacity": 1,
    "padding": 24,
    "sibling_gap": 32,
    "shadow": false
  },
  "company": {
    "node": {
      "radius": 12,
      "fill_role": "sub",
      "fill_opacity": 1,
      "stroke_width": 2,
      "shadow": false
    },
    "container": {
      "radius": 12,
      "fill_role": "background",
      "fill_opacity": 1,
      "padding": 28,
      "shadow": {
        "dx": 0,
        "dy": 4,
        "sigma": 10,
        "opacity": 0.15
      }
    },
    "quote_panel": {
      "radius": 12,
      "fill_opacity": 1,
      "shadow": {
        "dx": 0,
        "dy": 4,
        "sigma": 7.5,
        "opacity": 0.2
      }
    },
    "kpi": {
      "radius": 14,
      "fill_opacity": 1,
      "padding": 20,
      "shadow": false
    },
    "process": {
      "radius": 32,
      "height": 64,
      "fill_opacity": 1,
      "shadow": false
    },
    "spacing": {
      "padding": 24,
      "heading_gap": 16,
      "node_gap": 32,
      "group_gap": 48,
      "connector_label_clearance": 8
    },
    "density": {
      "compact": {
        "padding": 16,
        "node_gap": 24,
        "group_gap": 32
      },
      "regular": {
        "padding": 24,
        "node_gap": 32,
        "group_gap": 48
      },
      "spacious": {
        "padding": 32,
        "node_gap": 48,
        "group_gap": 64
      }
    },
    "optional_group_fill": {
      "role": "main",
      "fill_opacity": 0.12,
      "stroke_opacity": 1,
      "text_opacity": 1,
      "status": "新規図解用の提案。重なりと背景ごとに確認。標準ノードには自動適用しない。"
    }
  },
  "evidence": {
    "observed": [
      "business:カード角丸12、内側28、影dy4/sigma10/黒15%",
      "voices:白パネル角丸12、影dy4/sigma7.5/黒20%",
      "culture:KPI角丸14、内側20、影なし",
      "selection:ピル高さ64・半径32、影なし"
    ],
    "proposed": [
      "新規ノードの角丸12",
      "compact/regular/spaciousの密度差",
      "グループ背景の半透明12%"
    ]
  },
  "application": "共通原則 → Companyスタイル → 部品固有の例外 → 原稿の配置。背景4パターンの透明度は背景素材の値を保持。",
  "drawing": {
    "id": "style-profiles",
    "title": "同じ図解にテンプレート別スタイルを適用",
    "canvas": [
      1600,
      550
    ],
    "nodes": [
      {
        "type": "rect",
        "x": 0,
        "y": 0,
        "w": 1600,
        "h": 550,
        "fill_role": "background"
      },
      {
        "type": "text",
        "x": 44,
        "y": 26,
        "w": 470,
        "h": 54,
        "text": "Standard",
        "size": 30,
        "leading": 45.0,
        "fill_role": "text",
        "weight": 700
      },
      {
        "type": "rect",
        "x": 44,
        "y": 104,
        "w": 472,
        "h": 300,
        "fill_role": "background",
        "rx": 4,
        "stroke_role": "line",
        "stroke-width": 1,
        "filter": "none"
      },
      {
        "type": "rect",
        "x": 68,
        "y": 132,
        "w": 424,
        "h": 110,
        "fill_role": "sub",
        "rx": 4,
        "fill-opacity": 1
      },
      {
        "type": "text",
        "x": 84,
        "y": 150,
        "w": 372,
        "h": 70,
        "text": "構図と意味は共通\n変えるのはスタイル",
        "size": 24,
        "leading": 34,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "text",
        "x": 68,
        "y": 274,
        "w": 420,
        "h": 86,
        "text": "角丸 4px / 塗り 100%\n余白 24px / 部品間 32px",
        "size": 22,
        "leading": 32,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "text",
        "x": 44,
        "y": 430,
        "w": 472,
        "h": 96,
        "text": "影なし・フラット",
        "size": 22,
        "leading": 32,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "text",
        "x": 564,
        "y": 26,
        "w": 470,
        "h": 54,
        "text": "Company",
        "size": 30,
        "leading": 45.0,
        "fill_role": "text",
        "weight": 700
      },
      {
        "type": "rect",
        "x": 564,
        "y": 104,
        "w": 472,
        "h": 300,
        "fill_role": "background",
        "rx": 12,
        "stroke_role": "line",
        "stroke-width": 1,
        "filter": "url(#company-shadow)"
      },
      {
        "type": "rect",
        "x": 592,
        "y": 132,
        "w": 416,
        "h": 110,
        "fill_role": "sub",
        "rx": 12,
        "fill-opacity": 1
      },
      {
        "type": "text",
        "x": 608,
        "y": 150,
        "w": 364,
        "h": 70,
        "text": "構図と意味は共通\n変えるのはスタイル",
        "size": 24,
        "leading": 34,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "text",
        "x": 592,
        "y": 274,
        "w": 420,
        "h": 86,
        "text": "角丸 12px / 塗り 100%\n余白 28px / 部品間 32px",
        "size": 22,
        "leading": 32,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "text",
        "x": 564,
        "y": 430,
        "w": 472,
        "h": 96,
        "text": "まとまりの外側にだけ影\ndy 4 / σ10 / 黒15%",
        "size": 22,
        "leading": 32,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "text",
        "x": 1084,
        "y": 26,
        "w": 470,
        "h": 54,
        "text": "Company / compact",
        "size": 30,
        "leading": 45.0,
        "fill_role": "text",
        "weight": 700
      },
      {
        "type": "rect",
        "x": 1084,
        "y": 104,
        "w": 472,
        "h": 300,
        "fill_role": "background",
        "rx": 12,
        "stroke_role": "line",
        "stroke-width": 1,
        "filter": "none"
      },
      {
        "type": "rect",
        "x": 1100,
        "y": 132,
        "w": 440,
        "h": 110,
        "fill_role": "main",
        "rx": 12,
        "fill-opacity": 0.12
      },
      {
        "type": "text",
        "x": 1116,
        "y": 150,
        "w": 388,
        "h": 70,
        "text": "構図と意味は共通\n変えるのはスタイル",
        "size": 24,
        "leading": 34,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "text",
        "x": 1100,
        "y": 274,
        "w": 420,
        "h": 86,
        "text": "角丸 12px / 塗り 12%\n余白 16px / 部品間 24px",
        "size": 22,
        "leading": 32,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "text",
        "x": 1084,
        "y": 430,
        "w": 472,
        "h": 96,
        "text": "影なし・フラット",
        "size": 22,
        "leading": 32,
        "fill_role": "text",
        "weight": 400
      }
    ],
    "shadows": {
      "company-shadow": {
        "dx": 0,
        "dy": 4,
        "sigma": 10,
        "opacity": 0.15
      }
    }
  }
}
```
