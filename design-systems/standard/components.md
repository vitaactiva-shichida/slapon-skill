<!-- Generated from index.html#components. Edit index.html, not this file. -->

## コンポーネントからページを組み立てる

ページは完成図を丸ごと選ぶ前に、背景・ヘッダー・タイトル・本文グリッド・内容部品・フッターへ分けて設計する。下表から各部品の仕様と背景別の見本を確認する。

[H01**ヘッダー**上段のカテゴリ・パンくず・ロゴ・罫線](components/header.md)[F01**フッター**発行元・出典・ページ番号と背景別の色](components/footer.md)[T01**文字とフォント**書体・太さ・サイズ・行送り・縮小の限度](components/typography.md)[G01–G06**カラム**12カラム基準と均等・非対称の割り付け](components/grid.md)[BG01–BG05**背景**全面と左右の色面。本文カラムから独立](components/background.md)[DIAGRAM**図解の共通ルール**余白・色・透明度・形・線](components/diagram-rules.md)[SVG-LAYERS**重なり・面・色**SVGの描画順と色役割を正確に継承](components/layered-diagrams.md)[P03-SVG**連続シェブロン**工程帯・円形アイコン・説明のSVG](components/process-flow.md)[P01–P08**本文の部品**カード・アイコン・工程・関係図・数値](components/primitives.md)[D01**表紙の縦ロゴ透かし**右端の大きい白ロゴ・回転・不透明度40%](components/cover-watermark.md)[D02**メッセージの縦ロゴ透かし**表紙より小さく右下へ・不透明度40%](components/message-watermark.md)[R01–R03**ページの組立**部品を選んで情報関係に合うページへ](composition.md)

BCG版制作キットの「固定／許容範囲／自由領域」「カラムと背景の分離」「フォントを段階的に調整」の考え方を参照。値・色・書体・ヘッダー素材はStandard用に定義する。

仕様データ

```
{
  "canvas": [
    1600,
    900
  ],
  "order": [
    "background",
    "header",
    "title",
    "body_grid",
    "content_components",
    "footer"
  ],
  "fixed": [
    "header anchors",
    "footer anchors",
    "logo aspect ratio"
  ],
  "flexible": [
    "column count",
    "body internal geometry",
    "background division"
  ],
  "detail_references": {
    "H01": "ヘッダー",
    "F01": "フッター",
    "T01": "文字とフォント",
    "G01–G06": "カラム",
    "BG01–BG05": "背景",
    "P01–P08": "本文の部品",
    "R01–R03": "ページの組立",
    "D01": "表紙の縦ロゴ透かし",
    "D02": "メッセージの縦ロゴ透かし",
    "DIAGRAM": "図解の共通ルール",
    "SVG-LAYERS": "重なり・面・色の精密なSVG",
    "P03-SVG": "連続シェブロンの工程図"
  },
  "basis": "Standard原本の固定値と、再構成用の提案を区別する。"
}
```
