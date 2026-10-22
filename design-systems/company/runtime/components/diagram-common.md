<!-- Generated from index.html#diagram-common. Edit index.html, not this file. -->

## 図解の共通原則｜構図・意味・重なり・編集単位

図解の意味の組み立て方は共通です。テンプレート間で変えるのは角丸・塗りの透明度・余白・影などのスタイルです。同じ図解構造に別のスタイルを適用できます。

| 対象 | 共通ルール |
| --- | --- |
| 構図 | 伝える関係から選び、ノード数・工程数・項目数は原稿に合わせる。 |
| 色 | 同じ意味は同じ役割色。色だけで分類せず、ラベルや線種も対応させる。 |
| 文字 | 不透明100%。同一スタイルの段落は一つの編集単位にする。 |
| 接続 | 関連は線、順序や移動は矢印。文字の背後へ線を通さない。 |
| 透明度 | 塗りだけへ設定し、文字や輪郭をまとめて薄くしない。重なりの合成色も確認する。 |
| 重なり | 背面→接続→ノード→アイコン→文字。手前が不透明な場合は背面を正しく隠す。 |
| 編集 | デザイン確認後、図解部分だけをSVG化。ページの文字・ヘッダー・フッターはPowerPointの要素として組む。 |

仕様データ

```
{
  "id": "diagram-common-v1",
  "canvas": [
    1600,
    900
  ],
  "basis": "Standardの図解定義と2026-10-21の利用者指示から抽出した共通原則。テンプレートの造形値は別のstyle_profileへ置く。",
  "semantics": {
    "pattern": "関係に合わせて比較・順序・並列・包含・中心と周辺・集約と分岐から選ぶ",
    "same_meaning_same_color": true,
    "number_of_nodes": "原稿に合わせて可変",
    "color_not_only_signal": true
  },
  "text": {
    "opacity": 1,
    "paragraph_unit": "同一スタイルの段落は一つのテキストボックス。改行はボックス内で保持",
    "overflow": "要約・領域拡大・配置変更・分割。無断省略しない"
  },
  "connectors": {
    "meaning": "関連は線、順序・移動は矢印",
    "avoid_crossing_labels": true,
    "anchors": "接続先の輪郭へそろえる"
  },
  "layers": {
    "order": [
      "装飾・グループ面",
      "接続線",
      "ノードの面",
      "アイコン",
      "文字"
    ],
    "foreground_occlusion": "手前の説明ノードは背面を隠す。意図しない輪郭の透けを防ぐ",
    "fill_opacity": "テンプレートの指定値をfill-opacityへ設定する。文字を含む親グループには設定しない",
    "alpha_composite": "重なりの合成色を確認。意味を示す色は背景と組にして定義"
  },
  "style_profile_keys": [
    "radius",
    "fill_opacity",
    "padding",
    "node_gap",
    "group_gap",
    "shadow",
    "stroke"
  ],
  "precision": "viewBox、ネイティブ寸法、描画順、接続点、線幅、塗りと輪郭の役割を保持。構図と要素数は固定しない。",
  "editing_boundary": {
    "svg_scope": "図解部分だけ",
    "native_powerpoint_elements": [
      "ヘッダー",
      "タイトル",
      "本文",
      "フッター"
    ],
    "whole_page_svg": false
  }
}
```
