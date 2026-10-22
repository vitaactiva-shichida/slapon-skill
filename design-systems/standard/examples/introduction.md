<!-- Generated from index.html#page-introduction. Edit index.html, not this file. -->

## 組合せ例 05｜説明＋写真

固定のページ型ではなく、図解部品の組み合わせ例。[共通ルール](../components/diagram-rules.md)に沿って部品数・配置・原稿量を調整する。

### 使用するコンポーネント

| 背景 | ヘッダー | 文字 | グリッド | 本文・主役 | フッター |
| --- | --- | --- | --- | --- | --- |
| BG01 | H01-Light | T01＋T03＋箇条書き | 左680・間48・右712 | P06＋T02＋T03 | F01-Light |

詳しい説明と写真を並べる

![サービス紹介の文字入り見本](../assets/previews/introduction.svg)

図解共通ルールを適用した再構成見本。文章・数値は原本のサンプルを保持。新しい資料の原稿ではありません。

上段にT01の本文タイトル。下段は左に段落・箇条書き、右に写真。本文680px・間隔48px・写真712px。

### 可変領域・収まらないとき

説明と写真は別々に入れ替えられる

写真未提供なら原本の人物を顧客社員として使わない。説明を主役に再配分。

過去原本の読取座標（新見本の配置は仕様drawingに記載）

過去原本のレイヤー読取値は比較用に保持する。05〜12の再構成後の配置はdrawingの座標を使い、古い枠へ機械的に文字を押し込まない。

| 要素 | x | y | w | h | 扱い |
| --- | --- | --- | --- | --- | --- |
| カテゴリ | 30 | 25 | 167 | 26 | 原本サンプル。文字は差替え |
| 区切り | 209 | 25 | 8 | 26 | 原本サンプル。文字は差替え |
| パンくず | 229 | 25 | 1020 | 26 | 原本サンプル。文字は差替え |
| Lead | 80 | 229 | 660 | 128 | 原本サンプル。文字は差替え |
| Body1 | 80 | 385 | 660 | 117 | 原本サンプル。文字は差替え |
| Body2 | 80 | 530 | 660 | 117 | 原本サンプル。文字は差替え |
| Body3 | 80 | 675 | 660 | 39 | 原本サンプル。文字は差替え |
| 著作権 | 30 | 860 | 800 | 17 | 原本サンプル。文字は差替え |
| ページ | 1520 | 860 | 55 | 17 | 原本サンプル。文字は差替え |

仕様データ

```
{
  "id": "introduction",
  "template_node": "45:28106",
  "purpose": "詳しい説明と写真を並べる",
  "recipe": "上段にT01の本文タイトル。下段は左に段落・箇条書き、右に写真。本文680px・間隔48px・写真712px。",
  "overflow": "写真未提供なら原本の人物を顧客社員として使わない。説明を主役に再配分。",
  "reference_nodes": [
    {
      "name": "カテゴリ",
      "type": "TEXT",
      "text": "SERVICE SAMPLE",
      "x": 30,
      "y": 25,
      "w": 167,
      "h": 26
    },
    {
      "name": "区切り",
      "type": "TEXT",
      "text": "•",
      "x": 209,
      "y": 25,
      "w": 8,
      "h": 26
    },
    {
      "name": "パンくず",
      "type": "TEXT",
      "text": "Slapon  •  AIとつくる資料作成",
      "x": 229,
      "y": 25,
      "w": 1020,
      "h": 26
    },
    {
      "name": "Lead",
      "type": "TEXT",
      "text": "伝えたいことに、\nもっと時間を。",
      "x": 80,
      "y": 229,
      "w": 660,
      "h": 128
    },
    {
      "name": "Body1",
      "type": "TEXT",
      "text": "Slaponは、情報整理から仕上げまで、資料づくりの工程を支えます。入力した情報をもとにAIが初稿をつくり、人は伝える内容の検討と微調整に集中できます。",
      "x": 80,
      "y": 385,
      "w": 660,
      "h": 117
    },
    {
      "name": "Body2",
      "type": "TEXT",
      "text": "・伝える順番を整理する\n・関係を図解で示す\n・文字と余白を揃える",
      "x": 80,
      "y": 530,
      "w": 660,
      "h": 117
    },
    {
      "name": "Body3",
      "type": "TEXT",
      "text": "※ サービス紹介のデザイン検討用サンプル。",
      "x": 80,
      "y": 675,
      "w": 660,
      "h": 39
    },
    {
      "name": "著作権",
      "type": "TEXT",
      "text": "© 2026 Slapon Inc.",
      "x": 30,
      "y": 860,
      "w": 800,
      "h": 17
    },
    {
      "name": "ページ",
      "type": "TEXT",
      "text": "03",
      "x": 1520,
      "y": 860,
      "w": 55,
      "h": 17
    }
  ],
  "geometry_status": "既存レイヤー読取情報。アウトラインのインク外接矩形と異なる場合がある。改行後はプレビュー照合。",
  "canvas": [
    1600,
    900
  ],
  "composition": {
    "background": "BG01",
    "header": "H01-Light",
    "typography": "T01＋T03＋箇条書き",
    "grid": "2カラム / 左680・間48・右712",
    "content": "P06＋T02＋T03",
    "footer": "F01-Light"
  },
  "composition_geometry_policy": "新しい作例はdrawingの座標で再構成。reference_nodesは過去原本の読取値で、新見本の配置値ではない。",
  "classification": "composition_example",
  "fixed_page_template": false,
  "reusable_components": "P06＋T02＋T03",
  "adaptation": "説明と写真は別々に入れ替えられる",
  "common_rules": "components/diagram-rules.md",
  "drawing": {
    "canvas": [
      1600,
      900
    ],
    "nodes": [
      {
        "type": "text",
        "x": 30,
        "y": 25,
        "w": 168.0,
        "h": 30,
        "text": "SERVICE SAMPLE",
        "size": 20,
        "role": "text",
        "line_height": 26,
        "align": "left",
        "font-weight": 700
      },
      {
        "type": "line",
        "x1": 218.0,
        "x2": 218.0,
        "y1": 28.0,
        "y2": 48.0,
        "role": "muted",
        "stroke-width": 1
      },
      {
        "type": "text",
        "x": 239.0,
        "y": 25,
        "w": 1197.0,
        "h": 30,
        "text": "Slapon  •  AIとつくる資料作成",
        "size": 20,
        "role": "text",
        "line_height": 26,
        "align": "left",
        "font-weight": 700
      },
      {
        "type": "line",
        "x1": 30,
        "y1": 68,
        "x2": 1570,
        "y2": 68,
        "role": "line",
        "stroke-width": 1
      },
      {
        "type": "rect",
        "x": 30,
        "y": 67,
        "width": 64,
        "height": 3,
        "rx": 0,
        "role": "main"
      },
      {
        "type": "text",
        "x": 80,
        "y": 114,
        "w": 1440,
        "h": 50,
        "text": "伝えたいことに、もっと時間を。",
        "size": 42,
        "role": "text",
        "line_height": 50,
        "align": "left",
        "font-weight": 700
      },
      {
        "type": "text",
        "x": 1520,
        "y": 861,
        "w": 55,
        "h": 22,
        "text": "05",
        "size": 14,
        "role": "text",
        "line_height": 20,
        "align": "right"
      },
      {
        "type": "text",
        "x": 80,
        "y": 248,
        "w": 680,
        "h": 117,
        "text": "Slaponは、情報整理から仕上げまで、資料づくりの工程を支えます。入力した情報をもとにAIが初稿をつくり、人は伝える内容の検討と微調整に集中できます。",
        "size": 26,
        "role": "text",
        "line_height": 39,
        "align": "left"
      },
      {
        "type": "text",
        "x": 80,
        "y": 397,
        "w": 680,
        "h": 126,
        "text": "・伝える順番を整理する\n・関係を図解で示す\n・文字と余白を揃える",
        "size": 26,
        "role": "text",
        "line_height": 42,
        "align": "left"
      },
      {
        "type": "text",
        "x": 80,
        "y": 555,
        "w": 680,
        "h": 52,
        "text": "※ サービス紹介のデザイン検討用サンプル。",
        "size": 18,
        "role": "muted",
        "line_height": 26,
        "align": "left"
      },
      {
        "type": "image",
        "x": 808,
        "y": 248,
        "width": 712,
        "height": 464,
        "href": "/assets/apply/templates/slapon-01/photo-05-color.png",
        "preserveAspectRatio": "xMidYMid slice"
      }
    ],
    "header_layout": "H01 content_width; separator gaps 20px, glyph-center alignment",
    "title_spacing": "T01 y114 h50; subtitle y176 (12px gap)"
  },
  "rendering_basis": "2026-10-21利用者指示による図解共通ルール適用後の再構成見本。原本はassets/sourceに保存。",
  "applied_rules": {
    "column_gap": 48,
    "text_width": 680,
    "photo_box": [
      808,
      248,
      712,
      464
    ],
    "opacity": 1,
    "header_long_category_size": 17,
    "paragraph_to_list_gap": 32,
    "footer_baseline": 875
  }
}
```
