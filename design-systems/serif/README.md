# Slapon Serif デザイン原本

index.htmlがルールと見本の組み合わせを定義するHTML正本です。二重波括弧は設定・素材の挿入位置です。ここを直接開くのではなく、templates/design-system/serif/preview/index.htmlで描画済みの見本を確認します。

- assets/source/：保持したFigmaのSVG。元座標・文字・描画順を保持。編集済みプレビューをこの原本へ戻さない。
- assets/fonts/：指定書体とOFL。
- source-manifest.json：参照ノード、取得方法、保持素材のハッシュ。
- assets/backgrounds/：Serifの配色別PNG背景。Companyの背景はsource/内の曲線を保持して色替えする。

ルールはこのHTMLで編集します。仕様JSON・工程別Markdownはレンダラーで書き出す派生物です。顧客の正式設定や共有の制作手順はここへ複製しません。ロゴ追加位置と新規図解の余白・線幅は雛形としての運用ルールで、Figmaで測定した値と区別しています。
