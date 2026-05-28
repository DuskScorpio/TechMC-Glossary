<div align="center">

<!-- README-I18N:START -->

[English](./README.md) | [汉语](./README.zh.md) | [Русский](./README.ru.md) | **Español**

<!-- README-I18N:END -->

# TechMC Glossary

> Un glosario multilingüe de términos técnicos de Minecraft, pensado para ayudar a jugadores, desarrolladores y traductores a mantener una terminología coherente entre idiomas.

[Explorar el glosario en línea](http://beta.techmc.wiki/glossary) · [Ver el CSV fuente](https://github.com/DuskScorpio/TechMC-Glossary/blob/main/TechMC%20Glossary.csv)

</div>

## Idiomas disponibles

- Inglés
- Chino simplificado
- Ruso
- Español

## El archivo del glosario

`TechMC Glossary.csv` contiene las siguientes columnas:

| Columna | Propósito |
|---|---|
| `Category` | Agrupación temática (se usa para ordenar) |
| `Short Form` | Abreviatura común, si existe |
| `Regex` | Expresión regular opcional para términos con cantidades variables |
| `Full Form (English)` | Término canónico en inglés |
| `Related` | Enlaces a sinónimos y términos relacionados |
| `Description` | Definición en inglés |
| `<Idioma>` / `Description (<Idioma>)` | Traducción y definición localizada |

> [!NOTE]
> Las entradas controvertidas o pendientes se marcan con un `*` al final.

### Convenciones de la columna `Related`

La columna `Related` enlaza términos mediante prefijos tipados:

| Prefijo | Significado | Ejemplo |
|---|---|---|
| `synonym:` | Mismo concepto, nombre intercambiable | `synonym:Instant Tile Tick` |
| `see:` | Concepto distinto pero relacionado | `see:Comparator Update Detector` |

Las múltiples entradas se separan con `; `, por ejemplo:

```
synonym:Bounding Box; synonym:Hitbox; see:Collision Box
```

## Cómo contribuir

> [!TIP]
> Para la mayoría de las ediciones, el **[editor web en beta.techmc.wiki/glossary](http://beta.techmc.wiki/glossary)** es la opción más cómoda y la recomendada. Para cambios complejos o grandes, sigue siendo recomendable trabajar en local con `git` y el repositorio clonado.

Si prefieres trabajar directamente con el archivo:

- Abre un [issue](https://github.com/DuskScorpio/TechMC-Glossary/issues) para discutir un cambio o reportar un problema.
- Haz un fork del repositorio, edita `TechMC Glossary.csv` y envía un pull request.
- Mantén el formato consistente y explica tus razones en la descripción del PR.

### Editar el CSV manualmente

1. [Descarga `TechMC Glossary.csv`](https://github.com/DuskScorpio/TechMC-Glossary/raw/main/TechMC%20Glossary.csv) (clic derecho → Guardar como).
2. Ábrelo en Microsoft Excel, LibreOffice Calc o cualquier herramienta de hoja de cálculo.
3. Asegúrate de que las filas queden ordenadas alfabéticamente por la columna `Category`.
4. Guarda como **CSV UTF-8 (delimitado por comas) (`*.csv`)**.
5. Envía tus cambios mediante un pull request.

> [!IMPORTANT]
> Guarda siempre con codificación **UTF-8** para evitar problemas con caracteres no latinos.

## Créditos

La versión inicial de este glosario fue hecha a partir de las siguientes fuentes:

- [GraduateTextsInTechnicalMC](https://github.com/tanhHeng/GraduateTextsInTechnicalMC)
- [LAS TMC Translation](https://www.youtube.com/@redstonevideotranslation5478)
