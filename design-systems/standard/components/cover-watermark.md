<!-- Generated from index.html#component-watermark. Edit index.html, not this file. -->

## D01｜表紙：右側の縦ロゴ透かし

表紙は左に主題、右端に大きい縦ロゴの透かしを置く。左上の通常ロゴとは独立した部品で、**正式ロゴの白版を下から上に読む向きへ回転し、不透明度40%で重ねる。**文字では代用せず、ロゴの輪郭と縦横比を保つ。

![表紙右端の縦ロゴ透かしの見本](../assets/previews/cover.svg)

D01｜参照Figmaの配置枠・回転・白40%を継承。顧客版は同じ枠へ正式ロゴを収める。

| 項目 | 基準（1600×900参照px） | 扱い |
| --- | --- | --- |
| 配置枠 | x1337 / y−58 / w348 / h1021 | 右端からはみ出した部分はスライド境界でクリップ |
| 回転前のロゴ枠 | w1021 / h348 | 縦横比を保って内接。引き伸ばさない |
| 回転と位置 | translate(1337,963) → rotate(−90°) | 下から上に読む向き。左右反転はしない |
| 色と透過率 | 白 #FFFFFF / 不透明度40% | Figmaの塗りの実測値。輪郭の外は透明 |
| タイトルとの分離 | 主題は原本のx96・w1100を基準。x1337以右は透かし領域 | 文字・日付・別の図版を右端へ侵入させない |
| 左上の通常ロゴ | x96 / y86 / w208 / h57 | 不透明度100%。透かしと別の倍率・部品で保持 |

顧客版は余白を調整した正式ロゴの白版を使用する。元ロゴの縦横比がSlaponと異なるため、枠の中で見える輪郭幅は変わる。透かし用にロゴを描き直さず、同じ白版素材を使う。この部品は表紙用であり、本文・章扉・エンドへ自動追加しない。

[Figmaの表紙参照（107:8610）](https://www.figma.com/design/yZRuVrGDlV496zazD5AqGf/?node-id=107-8610)

仕様データ

```
{
  "id": "D01",
  "name": "表紙右側の縦ロゴ透かし",
  "pages": [
    "cover"
  ],
  "reference": {
    "fileKey": "yZRuVrGDlV496zazD5AqGf",
    "frameNodeId": "107:8610",
    "watermarkNodeId": "107:8626",
    "url": "https://www.figma.com/design/yZRuVrGDlV496zazD5AqGf/?node-id=107-8610"
  },
  "canvas": [
    1600,
    900
  ],
  "rotated_bounds": [
    1337,
    -58,
    348,
    1021
  ],
  "local_logo_box": [
    0,
    0,
    1021,
    348
  ],
  "translate": [
    1337,
    963
  ],
  "rotation_degrees_svg": -90,
  "opacity": 0.4,
  "fill": "#FFFFFF",
  "clip_to_slide": true,
  "preserve_aspect_ratio": "xMidYMid meet",
  "text_exclusion_x": 1337,
  "logo_variant": "white",
  "evidence": "枠・回転・白40%はFigmaの実測。顧客ロゴを同比率枠へ内接する点は顧客版の適用。",
  "header_logo_is_independent": true
}
```
