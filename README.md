# OMaster Community

[OMaster](https://github.com/iCurrer/OMaster) 独立的预设云端仓库

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

### 提交新预设

> [!IMPORTANT]
> 规则已迁移至独立仓库维护
> 
> 不要直接在 [OMaster 主仓库](https://github.com/iCurrer/OMaster) 提交 Pull Request

如果你想贡献新的调色预设：

1. 在 `presets.json` 中添加预设数据
2. ~~*在 `app/src/main/assets/images/` 中添加样片*~~（这个之后再说罢）
3. 提交 Pull Request

### 预设数据格式

```json
{
  "name": "预设名称",
  "coverPath": "images/cover.webp",
  "galleryImages": ["images/sample1.webp"],
  "author": "@作者",
  "mode": "auto",
  "filter": "滤镜类型",
  "softLight": "柔光强度",
  "tone": 0,
  "saturation": 0,
  "warmCool": 0,
  "cyanMagenta": 0,
  "sharpness": 0,
  "vignette": "关",
  "isNew": true
}
```