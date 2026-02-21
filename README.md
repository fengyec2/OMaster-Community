# OMaster Community

[OMaster](https://github.com/iCurrer/OMaster) 独立的预设云端仓库

> [!IMPORTANT]
> 云端预设已迁移至此仓库单独维护
> 
> 如果只是更新云端预设，不要直接在 [OMaster 主仓库](https://github.com/iCurrer/OMaster) 提交 Pull Request

## 🔗 订阅此规则

复制以下任意一个链接到 OMaster 即可使用本订阅规则

- jsDelivr 源（中国大陆推荐）

```txt
https://cdn.jsdelivr.net/gh/fengyec2/OMaster-Community@main/presets.json
```

- GitHub 源

```txt
https://raw.github.com/fengyec2/OMaster-Community/main/presets.json
```

## ❤️ 第三方订阅列表

> [!NOTE]
> 如果你希望你的规则出现在下方列表
>
> 请确保你的仓库带有 `omatser-subscription` 话题标签

见 [GitHub Topic](https://github.com/topics/omatser-subscription)

## 🤝 贡献指南

<details>
  <summary>提交 OPPO / 一加 / Realme 新预设</summary>

  ### 提交 OPPO / 一加 / Realme 新预设

  如果你想贡献新的调色预设：

  1. Fork 此仓库
  2. 在 `presets.json` 中添加预设数据
  3. ~~*在 `app/src/main/assets/images/` 中添加样片*~~（这个之后再说罢）
  4. 提交 Pull Request
   
  ### 预设数据格式

  ```json
  {
    "presets": [
      {
        "name": "富士胶片",
        "coverPath": "images/fsjp_01.webp",
        "galleryImages": [
          "images/fsjp_02.webp",
          "images/fsjp_03.webp"
        ],
        "author": "@OPPO影像",
        "mode": "auto",
        "iso": null,
        "shutterSpeed": null,
        "exposureCompensation": null,
        "colorTemperature": null,
        "colorHue": null,
        "whiteBalance": null,
        "colorTone": null,
        "filter": "复古 100%",
        "softLight": "无",
        "tone": 0,
        "saturation": 19,
        "warmCool": -5,
        "cyanMagenta": 0,
        "sharpness": 15,
        "vignette": "开",
        "shootingTips": "【环境建议】日间户外或光线充足的室内\n【场景推荐】街拍、人像、风景、建筑\n【拍摄要点】适合追求经典胶片质感的场景，色彩浓郁复古，建议寻找有光影对比的场景增强层次感",
        "sections": [
          {
            "title": "@string/section_color_grading",
            "items": [
              {
                "label": "@string/param_filter",
                "value": "复古 100%",
                "span": 2
              },
              {
                "label": "@string/param_soft_light",
                "value": "无",
                "span": 1
              },
              {
                "label": "@string/param_tone_curve",
                "value": "0",
                "span": 1
              },
              {
                "label": "@string/param_saturation",
                "value": "+19",
                "span": 1
              },
              {
                "label": "@string/param_warm_cool",
                "value": "-5",
                "span": 1
              },
              {
                "label": "@string/param_cyan_magenta",
                "value": "0",
                "span": 1
              },
              {
                "label": "@string/param_sharpness",
                "value": "15",
                "span": 1
              },
              {
                "label": "@string/param_vignette",
                "value": "开",
                "span": 2
              }
            ]
          }
        ]
      }
    ]
  }
  ```
</details>

<details>
  <summary>创建其他品牌专业相机的新预设</summary>

  ### 创建其他品牌专业相机的新预设

  如果你想为 **其他品牌** 的专业相机提供预设

  或是你手机的专业相机参数配置 **与 OMaster 默认预设不同**

  那么你可以 **完全自定义** 你的云端配置并应用于 OMaster！

  1. Fork 此仓库
  2. 在 `presets.json` 中添加预设数据
  3. ~~*在 `app/src/main/assets/images/` 中添加样片*~~（这个之后再说罢）
  4. 提交 Pull Request
   
  ### 预设数据格式

  ```json
  {
    "presets": [
      {
        "name": "Dynamic Test",
        "coverPath": "images/fsjp_01.webp",
        "author": "@Test",
        "mode": "pro",
        "filter": "Test 100%",
        "whiteBalance": null,
        "colorTone": null,
        "exposureCompensation": null,
        "softLight": "无",
        "tone": 0,
        "saturation": 0,
        "warmCool": 0,
        "cyanMagenta": 0,
        "sharpness": 0,
        "vignette": "关",
        "sections": [
          {
            "title": "Custom Section 1",
            "items": [
              {
                "label": "Test Param 1",
                "value": "Value 1",
                "span": 2
              },
              {
                "label": "Test Param 2",
                "value": "Value 2",
                "span": 1
              }
            ]
          },
          {
            "title": "Custom Section 2",
            "items": [
              {
                "label": "Test Param 3",
                "value": "Value 3",
                "span": 1
              }
            ]
          }
        ]
      }
    ]
  }
  ```


</details>