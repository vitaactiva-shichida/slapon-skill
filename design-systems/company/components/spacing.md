<!-- Generated from index.html#component-spacing. Edit index.html, not this file. -->

## 余白の密度｜狭い・標準・広いを使い分ける

図解の基本構造を変えず、テンプレートの密度として余白を調整します。Compactは同一グループ内の短いラベル、Regularは通常の説明、Spaciousは要素数の少ない主題を候補にします。

{{detail.spacing-density}}

文字サイズを共通にして余白の違いを可視化。情報が収まらないときにCompactを自動選択しない。

| 対象 | 標準 | 下限・例外 |
| --- | --- | --- |
| ノード内部 | 24px | 短いラベルで16px。元の事業カードは28px。 |
| 見出しと説明／アイコンとラベル | 16px | 同じ図の中で統一。 |
| 同一グループ内の部品間 | 32px | Compact 24px／Spacious 48px。 |
| 別グループ間 | 48px | Compact 32px／Spacious 64px。 |
| 線と文字の輪郭 | 8px以上 | 接続線を文字の背後へ通さない。 |
| ページの左右安全域 | 80px | 装飾背景だけ画面端まで。矢印とラベルも安全域へ含める。 |

仕様データ

```
{
  "inherits": "diagram-common-v1",
  "profiles": {
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
  "scale": [
    8,
    16,
    20,
    24,
    28,
    32,
    40,
    48,
    64,
    80
  ],
  "metrics": "余白は文字や図形の見える輪郭から測る。影は有効な内側余白に含めない。",
  "drawing": {
    "id": "spacing-density",
    "title": "余白密度を同じ文字サイズで比較",
    "canvas": [
      1600,
      520
    ],
    "nodes": [
      {
        "type": "rect",
        "x": 0,
        "y": 0,
        "w": 1600,
        "h": 520,
        "fill_role": "background"
      },
      {
        "type": "text",
        "x": 36,
        "y": 20,
        "w": 480,
        "h": 50,
        "text": "Compact",
        "size": 28,
        "leading": 42.0,
        "fill_role": "text",
        "weight": 700
      },
      {
        "type": "rect",
        "x": 36,
        "y": 92,
        "w": 472,
        "h": 280,
        "fill_role": "background",
        "rx": 12,
        "stroke_role": "line",
        "stroke-width": 2
      },
      {
        "type": "rect",
        "x": 52,
        "y": 108,
        "w": 440,
        "h": 60,
        "fill_role": "sub",
        "rx": 12
      },
      {
        "type": "text",
        "x": 64,
        "y": 116,
        "w": 388,
        "h": 40,
        "text": "共通の文字サイズ 24px",
        "size": 24,
        "leading": 36.0,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 52,
        "y": 192,
        "w": 440,
        "h": 60,
        "fill_role": "sub",
        "rx": 12
      },
      {
        "type": "text",
        "x": 64,
        "y": 200,
        "w": 388,
        "h": 40,
        "text": "余白だけを変える",
        "size": 24,
        "leading": 36.0,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "text",
        "x": 36,
        "y": 408,
        "w": 480,
        "h": 72,
        "text": "内側16px / 間隔24px",
        "size": 24,
        "leading": 36.0,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "text",
        "x": 556,
        "y": 20,
        "w": 480,
        "h": 50,
        "text": "Regular",
        "size": 28,
        "leading": 42.0,
        "fill_role": "text",
        "weight": 700
      },
      {
        "type": "rect",
        "x": 556,
        "y": 92,
        "w": 472,
        "h": 280,
        "fill_role": "background",
        "rx": 12,
        "stroke_role": "line",
        "stroke-width": 2
      },
      {
        "type": "rect",
        "x": 580,
        "y": 116,
        "w": 424,
        "h": 60,
        "fill_role": "sub",
        "rx": 12
      },
      {
        "type": "text",
        "x": 592,
        "y": 124,
        "w": 372,
        "h": 40,
        "text": "共通の文字サイズ 24px",
        "size": 24,
        "leading": 36.0,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 580,
        "y": 208,
        "w": 424,
        "h": 60,
        "fill_role": "sub",
        "rx": 12
      },
      {
        "type": "text",
        "x": 592,
        "y": 216,
        "w": 372,
        "h": 40,
        "text": "余白だけを変える",
        "size": 24,
        "leading": 36.0,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "text",
        "x": 556,
        "y": 408,
        "w": 480,
        "h": 72,
        "text": "内側24px / 間隔32px",
        "size": 24,
        "leading": 36.0,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "text",
        "x": 1076,
        "y": 20,
        "w": 480,
        "h": 50,
        "text": "Spacious",
        "size": 28,
        "leading": 42.0,
        "fill_role": "text",
        "weight": 700
      },
      {
        "type": "rect",
        "x": 1076,
        "y": 92,
        "w": 472,
        "h": 280,
        "fill_role": "background",
        "rx": 12,
        "stroke_role": "line",
        "stroke-width": 2
      },
      {
        "type": "rect",
        "x": 1108,
        "y": 124,
        "w": 408,
        "h": 60,
        "fill_role": "sub",
        "rx": 12
      },
      {
        "type": "text",
        "x": 1120,
        "y": 132,
        "w": 356,
        "h": 40,
        "text": "共通の文字サイズ 24px",
        "size": 24,
        "leading": 36.0,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "rect",
        "x": 1108,
        "y": 232,
        "w": 408,
        "h": 60,
        "fill_role": "sub",
        "rx": 12
      },
      {
        "type": "text",
        "x": 1120,
        "y": 240,
        "w": 356,
        "h": 40,
        "text": "余白だけを変える",
        "size": 24,
        "leading": 36.0,
        "fill_role": "text",
        "weight": 400
      },
      {
        "type": "text",
        "x": 1076,
        "y": 408,
        "w": 480,
        "h": 72,
        "text": "内側32px / 間隔48px",
        "size": 24,
        "leading": 36.0,
        "fill_role": "text",
        "weight": 400
      }
    ]
  }
}
```
