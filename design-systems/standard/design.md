<!-- Generated from index.html#design. Edit index.html, not this file. -->

## 基本設計・配色・文字

Standard v0.1.0。公開用テンプレート slapon-01 v1.0.3をもとに定義。以下の青は表示例「ソフトブルー」。顧客指定があれば、その保存済みresolvedThemeを優先する。

背景  
#FFFFFF

補助背景  
#EAF0FA

文字  
#17283F

プライマリー  
#2356A8

アクセント  
#D89B34

背景と補助面を広く取り、主色は図表・短い罫線・重点情報へ、アクセントは意味のある強調へ使う。毎ページに5色すべてを使う必要はない。同じ意味の要素は同じ色にそろえる。

| 固定領域・役割 | 座標・寸法（1600×900参照px） | 根拠・適用 |
| --- | --- | --- |
| 本文左右 | x80〜1520（幅1440） | 公開用テンプレート |
| カテゴリ | x30 / y25 / h26 | ヘッダー上段。長い章名はパンくず側へ |
| パンくず | x=カテゴリ実測右端+41 / y25 / h26 | カテゴリの文字幅に追従。縦線の左右に各20px（全角1文字相当） |
| 短い主色線 | x30 / y67 / w64 / h3 | アクセントではなく主色 |
| 本文タイトル | x80 / y114 / w1440 / h50 | 標準本文型。表紙・目次・メッセージ・中扉は別 |
| 説明文 | x80 / y176 / w1440 / h35〜105 | 行数に応じ、本文を下げる |
| フッター | x30 / y860 / w800 / h17 | 社名・出典等。連絡先を作らない |
| ページ番号 | x1520 / y860 / w55 / h17 | 右端。サンプルの03は引き継がない |

和文はNoto Sans JP、欧文はArimoを同梱。文字サイズと行間はアウトライン見本を再構成するための初期提案で、Figmaテキストスタイルの精密な抽出値とは区別する。書体代替はYu Gothic / Arial。置換時は字幅・改行・行数を確認。

| 役割 | 参照px | 太さ | 行間 | 使い方 |
| --- | --- | --- | --- | --- |
| 表紙タイトル | 76 | 700 | 1.18 | 最大3行。原本の視覚比率に合わせた初期提案 |
| 本文タイトル | 42 | 700 | 1.2 | 通常1行。2行なら本文の開始を下げる |
| リード・大きい本文 | 48 | 700 | 1.3 | 紹介・メッセージ等。本文タイトルと別の役割 |
| 小見出し | 30 | 700 | 1.3 | 比較列・工程・機能の名称 |
| 本文 | 26 | 400 | 1.5 | 詳しい説明は24〜28px。列幅に合わせて再配置 |
| 図表ラベル | 22 | 400 | 1.3 | 系列名・軸・値。本文の代用にしない |
| 補足・注記 | 16 | 400 | 1.4 | 出典・但し書きのみ |
| ヘッダー | 20 | 700 | 1.3 | 上段カテゴリとパンくず |
| 発行元 | 15 | 400 | 17px | 基準線875pxにそろえる |
| ページ番号 | 14 | 400 | 17px | 右端1575px、基準線875px |
| 主役のKPI | 88 | 700 | 1.05 | 数値・単位を独立オブジェクトにする |

仕様データ

```
{
  "id": "slapon-standard",
  "version": "0.1.0",
  "template_id": "slapon-01",
  "template_version": "1.0.3",
  "canvas": {
    "width": 1600,
    "height": 900,
    "unit": "reference_px"
  },
  "example_palette": "blue",
  "fonts": {
    "jp": "Noto Sans JP",
    "latin": "Arimo",
    "fallback": "Yu Gothic / Arial"
  },
  "typography_basis": "再構成用の初期提案。SVGの文字はアウトライン化されておりフォントサイズの実測値ではない。",
  "type": [
    [
      "表紙タイトル",
      76,
      700,
      1.18,
      "最大3行。原本の視覚比率に合わせた初期提案"
    ],
    [
      "本文タイトル",
      42,
      700,
      1.2,
      "通常1行。2行なら本文の開始を下げる"
    ],
    [
      "リード・大きい本文",
      48,
      700,
      1.3,
      "紹介・メッセージ等。本文タイトルと別の役割"
    ],
    [
      "小見出し",
      30,
      700,
      1.3,
      "比較列・工程・機能の名称"
    ],
    [
      "本文",
      26,
      400,
      1.5,
      "詳しい説明は24〜28px。列幅に合わせて再配置"
    ],
    [
      "図表ラベル",
      22,
      400,
      1.3,
      "系列名・軸・値。本文の代用にしない"
    ],
    [
      "補足・注記",
      16,
      400,
      1.4,
      "出典・但し書きのみ"
    ],
    [
      "ヘッダー",
      20,
      700,
      1.3,
      "上段カテゴリとパンくず"
    ],
    [
      "発行元",
      15,
      400,
      1.1333333333333333,
      "基準線875px"
    ],
    [
      "ページ番号",
      14,
      400,
      1.2142857142857142,
      "右端1575px、基準線875px"
    ],
    [
      "主役のKPI",
      88,
      700,
      1.05,
      "数値・単位を独立オブジェクトにする"
    ]
  ],
  "layout": {
    "body_left": 80,
    "body_right": 1520,
    "header_category": [
      30,
      25,
      40,
      26
    ],
    "breadcrumb_x": "category visible right + 41",
    "short_rule": [
      30,
      67,
      64,
      3
    ],
    "title": [
      80,
      114,
      1440,
      50
    ],
    "subtitle": [
      80,
      176,
      1440,
      35
    ],
    "footer": [
      30,
      860,
      800,
      17
    ],
    "page_number": [
      1520,
      860,
      55,
      17
    ],
    "header_layout": "content_width; gaps20; separator1x20 centered on visible glyphs"
  },
  "geometry_basis": "1600×900公開用SVGと既存レイヤー読み取り情報。本文量に応じる可変領域は固定しない。レイヤー読取値はアウトラインのインク外接矩形と一致しない場合がある。",
  "typography_details": "specs/components/typography.json"
}
```

18配色の見本

ブルー `vivid-blue`

グリーン `vivid-green`

レッド `vivid-red`

オレンジ `vivid-orange`

パープル `vivid-purple`

ピンク `vivid-pink`

ソフトブルー `blue`

ソフトグリーン `green`

コーラル `coral`

チャコール `charcoal`

ネイビー `navy`

ティール `teal`

ミント `mint`

ラベンダー `lavender`

ローズ `rose`

サンド `sand`

オリーブ `olive`

ボルドー `burgundy`

表示例の派生色

| 役割 | コード |
| --- | --- |
| background | #FFFFFF |
| sub | #EAF0FA |
| text | #17283F |
| inkSurface | #17283F |
| main | #2356A8 |
| accent | #D89B34 |
| onmain | #FFFFFF |
| gradientEnd | #5877A9 |
| onSeries2 | #000000 |
| onSeries3 | #000000 |
| onSeries4 | #000000 |
| white | #FFFFFF |
| whiteMain | #2356A8 |
| comparisonMain | #2356A8 |
| comparisonText | #FFFFFF |
| conceptBackdrop | #F7F9FC |
| conceptRingOuter | #E8EDF6 |
| conceptRingInner | #DDE5F2 |
| conceptRingStroke | #B4C5E1 |
| muted | #6B7584 |
| mutedSurface | #616E7F |
| primaryInk | #2356A8 |
| primaryInkSurface | #2356A8 |
| accentInk | #996E25 |
| accentInkSurface | #8C6522 |
| line | #CCD0D5 |
| series2 | #7D9BCD |
| series3 | #B8CAE6 |
| series4 | #D2DEF0 |
