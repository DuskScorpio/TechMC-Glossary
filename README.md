<div align="center">

<!-- README-I18N:START -->

**English** | [汉语](./README.zh.md) | [Русский](./README.ru.md) | [Español](./README.es.md)

<!-- README-I18N:END -->

# TechMC Glossary

> A multilingual glossary of Minecraft technical terms, helping players, developers, and translators keep terminology consistent across languages.

[Browse the glossary online](http://beta.techmc.wiki/glossary) · [View the source CSV](https://github.com/DuskScorpio/TechMC-Glossary/blob/main/TechMC%20Glossary.csv)

</div>

## Available languages

- English
- Chinese (Simplified)
- Russian
- Spanish

## The glossary file

`TechMC Glossary.csv` contains the following columns:

| Column | Purpose |
|---|---|
| `Category` | Topical grouping (used for sorting) |
| `Short Form` | Common abbreviation, if any |
| `Regex` | Optional regex for variable-quantity terms |
| `Full Form (English)` | Canonical English term |
| `Related` | Links to synonyms and related terms |
| `Description` | English definition |
| `<Language>` / `Description (<Language>)` | Translation and localized definition |

> [!NOTE]
> Controversial or pending entries are marked with a trailing `*`.

### `Related` column conventions

The `Related` column links terms using typed prefixes:

| Prefix | Meaning | Example |
|---|---|---|
| `synonym:` | Same concept, interchangeable name | `synonym:Instant Tile Tick` |
| `see:` | Different but related concept | `see:Comparator Update Detector` |

Multiple entries are separated by `; `, for example:

```
synonym:Bounding Box; synonym:Hitbox; see:Collision Box
```

## Contributing

> [!TIP]
> For most edits, the **[web editor at beta.techmc.wiki/glossary](http://beta.techmc.wiki/glossary)** is the most convenient option and is recommended. For complex or large changes, working locally with `git` and the cloned repository is still advised.

If you'd rather work with the file directly:

- Open an [issue](https://github.com/DuskScorpio/TechMC-Glossary/issues) to discuss a change or report a problem.
- Fork the repo, edit `TechMC Glossary.csv`, and submit a pull request.
- Keep formatting consistent and explain your reasoning in the PR description.

### Editing the CSV manually

1. [Download `TechMC Glossary.csv`](https://github.com/DuskScorpio/TechMC-Glossary/raw/main/TechMC%20Glossary.csv) (right-click → Save As).
2. Open it in Microsoft Excel, LibreOffice Calc, or any spreadsheet tool.
3. Make sure rows stay sorted alphabetically by the `Category` column.
4. Save as **CSV UTF-8 (Comma delimited) (`*.csv`)**.
5. Submit your changes via a pull request.

> [!IMPORTANT]
> Always save in **UTF-8** encoding to avoid mojibake in non-Latin scripts.

## Credits

The initial version of this glossary was compiled from the following sources:

- [GraduateTextsInTechnicalMC](https://github.com/tanhHeng/GraduateTextsInTechnicalMC)
- [LAS TMC Translation](https://www.youtube.com/@redstonevideotranslation5478)
