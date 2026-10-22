# Standardデザインの適用

共通の工程はreferences/、Standardの定義はcustomer/。正本は管理元のdesign-systems/slapon-standard/index.html。顧客版の差分は管理元のcustomers/{id}/design-overrides.json。組立後のcustomer/index.htmlとMarkdownは派生物なので、管理元を直して再組立する。

構成・画像ではdesign.md、page-types.md、選んだ基本枠のpages/{id}.mdを読む。05〜12は固定ページ型ではなくexamples.mdとexamples/{id}.mdに分離した組み合わせ例。部品はcomponents.md、グラフはcharts.md、表はtables.md、文字はimage-typography.md、素材はassets.mdを追加。顧客設定customer-settings.mdが同梱されている場合は最初に読み、保存済みresolvedTheme・正式ロゴ・例外を優先する。

参照キャンバスは1600×900px。生成幅÷1600、またはPPTスライド幅pt÷1600で座標・寸法・文字を一緒に換算。960×540参照ptを使う他キットの数値と混ぜない。フォントサイズ等の提案値と原本観察を区別し、見本画像を実際に確認・添付する。

見本にはSlaponのサービス文・写真・ダミー数値が含まれる。新しい原稿へ流用しない。原本文字はアウトラインなので、PowerPointでは文字・単純図形・表・グラフをネイティブに再構築する。人物写真や複雑なSVGを画像として残す範囲は示す。ロゴは別素材として配置し、勝手に描き直さない。

長文は本文を省かず、配置・ページ分割で解決。画像採用の前提と既存の一括制作指示は共通工程に従う。HTML・SVGの描画確認と、新原稿の画像生成・PPTX・実機検証を別々に記録する。

## コンポーネントからページを組む

新しいページを設計するときはcomposition.mdとcomponents.mdを読み、背景、ヘッダー、タイトル、グリッド、内容部品、フッターを選ぶ。図解はまずcomponents/diagram-rules.mdを読み、余白・色・透明度・形・線を適用する。詳細はcomponents/header.md、footer.md、typography.md、grid.md、background.md、primitives.md。5つの基本枠はpages/{id}.md、05〜12の組み合わせ例はexamples/{id}.mdの部品一覧と原本の座標を併用する。05〜12は2026-10-21の利用者指示により図解共通ルールへ再構成した見本。配置はspecs/examples/{id}.json内drawingを使う。reference_nodesは変更前の原本読取値として残す。

背景の色面はスライド端まで塗り、文字・図は別の安全領域へ置く。濃色・淡色・左右分割のフッターは、文字の直下の背景色ごとに配色を選ぶ。タイトルが複数行になったら説明文と本文開始も下げ、本文を無断で削らない。

表紙ではcomponents/cover-watermark.mdを読み、左上ロゴと右側D01を別部品として扱う。顧客の白版ロゴを正式素材のまま−90°・不透明度40%で配置し、スライド境界でクリップする。

メッセージではcomponents/message-watermark.mdのD02とH01-Darkを適用する。図解の淡色面は色役割を不透明100%で塗り、文字・接続線を含むグループに透明度を設定しない。05〜12のカード数・工程数・列数・サンプル原稿は固定しない。

## SVGの精度とスタイル参照

図解ではcomponents/layered-diagrams.mdを読み、背景面・主役・白ノード・アイコン・文字の順と、手前の面が奥を隠す関係を保つ。紙を重ねたSVGの不透明な塗りを削除しない。構図と要素数は原稿から決め、中心＋周辺4つの形を固定テンプレートとして使わない。工程はcomponents/process-flow.mdの連続シェブロンを使う。参照由来の1.5／2.2／3px線幅と固有寸法を優先する。
