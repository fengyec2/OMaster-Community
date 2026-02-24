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

### JSON 格式

|       顶层键       |      描述      |      值      |
| ------------- | ------------- | ------------- |
| version | 预设数据格式版本，如无必要**请勿修改** | `2` |
| name | 预设的订阅显示名称 | 字符串 |
| author | 预设的订阅显示作者 | 字符串 |
| build | 预设的订阅显示版本，**值增加才会触发更新** | 整数 |

|  `presets` 内层键  |      描述      |      值      |
| ------------- | ------------- | ------------- |
| coverPath | App 首页封面图片 | 相对路径或 URL |
| galleryImages | 单个预设下轮播图片 | 相对路径或 URL |
| isNew | 是否为新配置 | `true` 置顶，非必须键 |

|  `sections` 内层键  |      描述      |      值      |
| ------------- | ------------- | ------------- |
| title | 预设配置的组名称 | 支持 `@string` 解析 |
| label | 组下单个预设配置的名称 | 支持 `@string` 解析 |
| span | 单个预设配置卡片宽度 | `1`: 半宽，`2`: 全宽 |

### 提交新预设

<details>
  <summary>提交 OPPO / 一加 / Realme 新预设</summary>

  #### 提交 OPPO / 一加 / Realme 新预设

  如果你想贡献新的调色预设：

  1. Fork 此仓库
  2. 新建一个分支（例如 `preset` ）
  3. 在新分支（例如 `preset` ）的 `presets.json` 中添加预设数据
  4. 在主分支（就是 `main` 分支）修改 README
  5. 提交 Pull Request，把你的新分支（例如 `preset` ）合并到 `fengyec2/OMaster-Community:main` 中
  
  > [!WARNING]
  > 不要把你的 README 更新也合并到上游仓库了
  >
  > 请确保你的 PR 只包含 `presets.json` 的更新
   
  #### 预设数据格式
  ```json
  {
    "version": 2,
    "name": "OPPO / 一加 / Realme 预设",
    "author": "@OMaster",
    "build": 3,
    "presets": [
      {
        "name": "富士胶片",
        "coverPath": "images/fsjp_01.webp",
        "galleryImages": [
          "images/fsjp_02.webp",
          "images/fsjp_03.webp"
        ],
        "author": "@OPPO影像",
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
        ],
        "tags": [
          "Auto"
        ],
        "description": {
          "title": "Shooting Tips",
          "content": "【环境建议】室外的室内\n【场景推荐】街拍、人像、风景、建筑\n【拍摄要点】适合追求五彩斑斓的黑质感的场景，色彩单调又丰富，建议寻找有光影对比的场景增强层次感"
        }
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
  2. 在 `presets.json` 中修改预设数据
  3. 在 `README.md` 中修改文档
  4. 将你的订阅链接发送给别人即可
   
  ### 预设数据格式

  ```json
  {
    "version": 2,
    "name": "新品牌 预设",
    "author": "@作者",
    "build": 1,
    "presets": [
      {
        "name": "新预设",
        "coverPath": "相对路径或URL",
        "galleryImages": [
          "相对路径或URL",
          "相对路径或URL"
        ],
        "author": "@作者",
        "sections": [
          {
            "title": "支持@string解析，这是一个大标题",
            "items": [
              {
                "label": "直接填参数名称也可以（如滤镜）",
                "value": "复古 100%",
                "span": 2
              },
              {
                "label": "柔光",
                "value": "无",
                "span": 1
              },
              {
                "label": "@string/param_tone_curve",
                "value": "0",
                "span": 1
              }
            ]
          },
          {
            "title": "这是另一个一个大标题",
            "items": [
              {
                "label": "直接填参数名称也可以（如滤镜）",
                "value": "复古 100%",
                "span": 2
              },
              {
                "label": "柔光",
                "value": "无",
                "span": 1
              },
              {
                "label": "@string/param_tone_curve",
                "value": "0",
                "span": 1
              }
            ]
          }
        ],
        "tags": [
          "Auto"
          "可以有多个"
        ],
        "description": {
          "title": "描述文本，也可以填拍摄建议",
          "content": "【环境建议】室外的室内\n【场景推荐】街拍、人像、风景、建筑\n【拍摄要点】适合追求五彩斑斓的黑质感的场景，色彩单调又丰富，建议寻找有光影对比的场景增强层次感"
        }
      }
    ]
  }
  ```
</details>