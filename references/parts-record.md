# 部品一覧のひな型

採用画像からページごとに作成します。案件・構成・採用記録を参照し、必要な部品だけ追加します。空の任意欄は削除できますが、再現に必要な属性は省略しません。

```
{
  "page": null,
  "job_ref": null,
  "plan_ref": null,
  "image_record_ref": null,
  "source_image": {
    "path": null,
    "width_px": null,
    "height_px": null
  },
  "output": {
    "width_pt": null,
    "height_pt": null
  },
  "reconstruction_scope": {
    "native_regions": [],
    "svg_regions": [],
    "image_regions": []
  },
  "intentional_changes": [],
  "parts": [
    {
      "id": "PART01",
      "role": null,
      "source_content_ref": null,
      "bbox_px": [
        null,
        null,
        null,
        null
      ],
      "z_order": null,
      "output_type": null,
      "edit_unit": null,
      "group_id": null,
      "content": {},
      "asset": {
        "decision": null,
        "path": null,
        "reason": null
      },
      "appearance": {},
      "connections": [],
      "editable_scope": null
    }
  ]
}
```

`reconstruction_scope`は素材制作前に記録する。各領域にID・範囲・形式を選んだ理由を含め、SVG領域は別テキストにするラベルも特定する。不要な領域は空配列でよい。実装で変われば理由とともに更新する。

### 部品の種類に応じて追加する内容

| 欄 | 記録するもの |
| --- | --- |
| content | 文字部品は正しい全文・改行。表やグラフは見出し・値・単位・系列、または作成時に解決できるデータ参照。 |
| asset | A＝再利用、B＝調整、C＝新規。素材ID・原本パス・出力パス、選択理由。Bは必要な変更、Cは既存素材を使えない理由。素材が不要なネイティブ図形は判断欄を省略。 |
| appearance | 共通スタイルは一度定義して参照可能。文字は書体・サイズ・太さ・字色・揃え・行間・内側余白。図形は塗り・線幅・角丸・透明度。必要ならグラデーションの方向と色、影、曲線・端点・矢尻、トリミング・素材比率を追加。寸法値には単位を付ける。 |
| connections | 線・矢印は始点と終点の部品ID、接続位置、意味・ラベル。接続しない部品は省略。 |
| SVGの場合 | SVGと、それを描画したPNG代替のパス。内部編集の可否は移動・差し替えと区別して記録。 |

bbox_pxは採用画像の左上原点[x,y,幅,高さ]です。PPT出力のptとは区別して換算します。位置・間隔・整列はbboxから判断できる値を重複記入せず、追加の拘束条件がある場合に記録します。必須条件と採用の根拠は参照する案件・画像記録に保持します。
