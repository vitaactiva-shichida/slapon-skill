<!-- Generated from index.html#component-message-watermark. Edit index.html, not this file. -->

## D02｜メッセージ：右側の縦ロゴ透かし

メッセージにも白版の縦ロゴを置く。表紙のD01より小さく、右下に寄せた専用の配置とする。回転は−90°、不透明度は40%。上段の通常ロゴは100%で独立して配置する。

![メッセージ右側の縦ロゴ透かしの見本](../assets/previews/message.svg)

D02｜指定Figmaの配置枠と白40%を継承。顧客版には正式ロゴの白版を適用。

| 項目 | 基準（1600×900参照px） | 扱い |
| --- | --- | --- |
| 回転後の配置枠 | x1421 / y242 / w236 / h693 | 右端と下端のはみ出しはスライド境界でクリップ |
| 回転前のロゴ枠 | w693 / h236 | 白版を縦横比を保って内接。引き伸ばさない |
| 回転と位置 | translate(1421,935) → rotate(−90°) | 下から上に読む向き |
| 色・不透明度 | #FFFFFF / 40% | 通常ロゴや主題の透明度は変更しない |
| 本文との分離 | x1421以右は透かし領域 | 新原稿は文字の実際の輪郭が領域に入らない幅で折り返す |
| ヘッダーロゴ | x1466 / y23 / w104 / h29 | H01-Darkの通常ロゴ。透かしとは別部品 |

表紙はD01、メッセージはD02を使い分ける。本文・章扉・エンドへは自動追加しない。元ロゴの縦横比が違うため、同じ枠でも実際の輪郭幅は異なる。

[Figmaのメッセージ参照（107:8650）](https://www.figma.com/design/yZRuVrGDlV496zazD5AqGf/?node-id=107-8650)

仕様データ

```
{
  "id": "D02",
  "name": "メッセージ右側の縦ロゴ透かし",
  "pages": [
    "message"
  ],
  "reference": {
    "fileKey": "yZRuVrGDlV496zazD5AqGf",
    "frameNodeId": "107:8650",
    "watermarkNodeId": "107:8659",
    "url": "https://www.figma.com/design/yZRuVrGDlV496zazD5AqGf/?node-id=107-8650"
  },
  "canvas": [
    1600,
    900
  ],
  "rotated_bounds": [
    1421,
    242,
    236,
    693
  ],
  "local_logo_box": [
    0,
    0,
    693,
    236
  ],
  "translate": [
    1421,
    935
  ],
  "rotation_degrees_svg": -90,
  "opacity": 0.4,
  "fill": "#FFFFFF",
  "clip_to_slide": true,
  "preserve_aspect_ratio": "xMidYMid meet",
  "text_exclusion_x": 1421,
  "logo_variant": "white",
  "evidence": "配置枠・回転・白40%は指定Figmaの実測。顧客ロゴの同比率枠への内接と本文の右端制限は再構成時の適用規則。",
  "header_logo_is_independent": true
}
```
