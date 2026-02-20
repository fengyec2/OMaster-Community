# OMaster Community

[OMaster](https://github.com/iCurrer/OMaster) 独立的预设云端仓库

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

### 提交新预设

> [!IMPORTANT]
> 云端预设已迁移至此仓库单独维护
> 
> 如果只是更新云端预设，不要直接在 [OMaster 主仓库](https://github.com/iCurrer/OMaster) 提交 Pull Request

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
      "name": "新预设",
      "coverPath": "images/新预设_01.webp",
      "galleryImages": [
        "images/新预设_02.webp",
        "images/新预设_03.webp"
      ],
      "author": "@作者",
      "mode": "auto",
      "iso": null,
      "shutterSpeed": null,
      "exposureCompensation": null,
      "colorTemperature": null,
      "colorHue": null,
      "whiteBalance": null,
      "colorTone": null,
      "filter": "滤镜类型",
      "softLight": "柔光强度",
      "tone": 0,
      "saturation": 19,
      "warmCool": -5,
      "cyanMagenta": 0,
      "sharpness": 15,
      "vignette": "开",
      "shootingTips": "【环境建议】XXXX\n【场景推荐】XX、XX、XX、XX\n【拍摄要点】适合追求XXXX感的场景，色彩XXXX，建议XXXX"
    }
  ]
}
```