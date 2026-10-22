<!-- Generated from index.html#component-chart. Edit index.html, not this file. -->

## S-CHART｜推移・構成比・KPI

[見本SVG](bar-chart.svg)

棒：幅42・ピッチ70、基線345。濃淡は原本の棒ごとの透明度。

[見本SVG](donut.svg)

構成比：色と凡例を同じ役割にそろえる。

[見本SVG](kpi.svg)

KPI：塗りつぶしたカードで囲まず、細い線と数値の階層で区切る。

| 部品 | 原本の基準 | 新規データへの対応 |
| --- | --- | --- |
| 棒グラフ | 0〜600を115px、棒幅42、ピッチ70 | 値から高さを再計算。期間・単位と0基線を明示。 |
| ドーナツ | 中心655,250／外半径85／内半径62.9 | 合計100%を確認し、系列と凡例の順序・色をそろえる。 |
| KPI | 110px幅、数値22pxセリフ、単位10px | 指標名・数値・単位・分母・期間を一組にする。 |

数値は架空の配置見本です。画像を変形して別の実績に見せず、元データから軸・棒・扇形を作り直します。背景の淡い色によって半透明の棒の見え方が変わるため、配色ごとに実寸で確認します。

仕様データ

```
{
  "canvas": [
    800,
    450
  ],
  "observed": {
    "bar": {
      "plot": [
        66,
        230,
        425,
        115
      ],
      "baseline": 345,
      "axis": [
        0,
        600
      ],
      "tick": 200,
      "width": 42,
      "pitch": 70,
      "radius": 0,
      "opacity": [
        0.38,
        0.48,
        0.58,
        0.68,
        0.78,
        1
      ],
      "value_size": 10,
      "period_size": 8,
      "sample_values": [
        120,
        180,
        270,
        360,
        480,
        600
      ]
    },
    "donut": {
      "center": [
        655,
        250
      ],
      "outer_radius": 85,
      "inner_radius": 62.9,
      "sample_values": [
        30,
        25,
        20,
        15,
        10
      ]
    },
    "kpi": {
      "width": 110,
      "pitch_x": 126,
      "pitch_y": 115,
      "number_size": 22,
      "font": "Libre Baskerville",
      "unit_size": 10,
      "label_size": 8,
      "filled_card": false,
      "shadow": false
    }
  },
  "policy": "値・単位・期間を明示し、元データから軸と形を計算。ドーナツの色と凡例を一致。影や丸いカードを追加しない。",
  "palette_fix": "原本に残っていた青固定の系列色を配色の同系色へ展開し、凡例の主色も図形と一致させる。原本SVGは保持。"
}
```
