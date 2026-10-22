<!-- Generated from index.html#component-footer. Edit index.html, not this file. -->

## C-F01｜フッター：発行元・ページ番号・出典

[見本SVG](footer-light.svg)

白背景：発行元とページ番号の右アンカーを保持。

[見本SVG](footer-color.svg)

背景色あり：文字の直下で濃淡を判断。余計な白帯や罫線を加えない。

| 要素 | 配置 | 規則 |
| --- | --- | --- |
| 発行元 | x20 / 基準線875.6 / 14px Regular | 正式社名・発行元。長い場合は正式な表示用名称を確認する。 |
| ページ番号 | 右端1580 / 基準線875.6 / 14px | 桁数が増えても右端を動かさない。 |
| 本文下端 | 新原稿はy820を目安 | 原本の実績ページは基準線826の節目説明を保持。新原稿へ無条件にコピーしない。 |
| 出典・注記（任意） | x80〜1520 / 基準線832 / 14pxを初期目安 | 長文なら本文領域を短くする。発行元とは別のテキストボックス。 |

左の発行元と右の番号は、背景の色が異なればそれぞれ判定します。淡色面はtext／inkSurface、主色面はonmain。背景の曲線を横切る場合は、文字を移すか背景パターンを選び直して可読性を保ちます。

仕様データ

```
{
  "id": "C-F01",
  "observed": {
    "region": [
      20,
      858,
      1560,
      24
    ],
    "company": {
      "x": 20,
      "baseline": 875.6,
      "size": 14,
      "weight": 400
    },
    "page": {
      "right": 1580,
      "baseline": 875.6,
      "size": 14,
      "align": "right"
    },
    "border": false
  },
  "proposed": {
    "body_bottom": 820,
    "optional_source": {
      "x": 80,
      "baseline": 832,
      "size": 14,
      "max_right": 1520
    },
    "local_surface_policy": "発行元とページ番号を別々に、その直下の背景で判断。"
  },
  "variants": [
    "light",
    "tint",
    "dark",
    "local-background"
  ],
  "omit_when": [
    "cover"
  ],
  "source_note": "出典は発行元の行に詰め込まず、本文末の別領域に置く。"
}
```
