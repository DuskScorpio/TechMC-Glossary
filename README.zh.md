<div align="center">

<!-- README-I18N:START -->

[English](./README.md) | **汉语** | [Русский](./README.ru.md) | [Español](./README.es.md)

<!-- README-I18N:END -->

# TechMC Glossary

> Minecraft 技术术语的多语言对照表，帮助技术玩家、开发者与翻译者在不同语言中保持术语一致。

[在线浏览术语表](http://beta.techmc.wiki/glossary) · [查看源 CSV 文件](https://github.com/DuskScorpio/TechMC-Glossary/blob/main/TechMC%20Glossary.csv)

</div>

## 可用语言

- 英文
- 简体中文
- 俄语
- 西班牙语

## 术语表文件

`TechMC Glossary.csv` 包含以下字段：

| 列名 | 用途 |
|---|---|
| `Category` | 主题分类（用于排序） |
| `Short Form` | 常用缩写（如有） |
| `Regex` | 用于可变数量术语的可选正则表达式 |
| `Full Form (English)` | 标准英文术语 |
| `Related` | 同义词和相关术语链接 |
| `Description` | 英文释义 |
| `<语言>` / `Description (<语言>)` | 译名与本地化释义 |

> [!NOTE]
> 存在争议或待商议的条目会在末尾标记 `*`。

### `Related` 列规范

`Related` 列使用类型前缀来链接关联术语：

| 前缀 | 含义 | 示例 |
|---|---|---|
| `synonym:` | 同义术语，可互换 | `synonym:Instant Tile Tick` |
| `see:` | 相关的不同术语 | `see:Comparator Update Detector` |

多个条目用 `; ` 分隔，例如：

```
synonym:Bounding Box; synonym:Hitbox; see:Collision Box
```

## 参与贡献

> [!TIP]
> 对于大多数改动，使用 **[beta.techmc.wiki/glossary 在线编辑器](http://beta.techmc.wiki/glossary)** 是最便捷的方式，推荐使用。对于较复杂或大规模的修改，仍建议在本地使用 `git` 克隆仓库后进行编辑。

如果你想直接修改文件：

- 通过 [Issues](https://github.com/DuskScorpio/TechMC-Glossary/issues) 讨论改动或反馈问题。
- Fork 本仓库，编辑 `TechMC Glossary.csv`，然后提交 Pull Request。
- 保持格式统一，并在 PR 描述中说明改动理由。

### 手动编辑 CSV

1. [下载 `TechMC Glossary.csv`](https://github.com/DuskScorpio/TechMC-Glossary/raw/main/TechMC%20Glossary.csv)（右键 → 另存为）。
2. 使用 Microsoft Excel、LibreOffice Calc 或其他表格工具打开。
3. 确保行按 `Category` 列字母顺序排列。
4. 保存为 **CSV UTF-8（逗号分隔） (`*.csv`)**。
5. 通过 Pull Request 提交修改。

> [!IMPORTANT]
> 请始终使用 **UTF-8** 编码保存，以避免非拉丁字符出现乱码。

## 致谢

本词汇表的初始版本参考了以下来源整理而成：

- [GraduateTextsInTechnicalMC](https://github.com/tanhHeng/GraduateTextsInTechnicalMC)
- [LAS TMC Translation](https://www.youtube.com/@redstonevideotranslation5478)
