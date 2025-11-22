## Description

This folder contains glossary sections, divided by category. Each category is represented by a CSV file named after the category, e.g., `slimestone.csv` for the "slimestone" category.

`_template.csv` provides the standard headers and format that all category CSV files should follow:

- CSV header changes should be applied to `_template.csv`; all category CSV files are then updated to conform to the revised headers.
- A new category should be created by copying `_template.csv`, to ensure correct file encodings.

## Criteria for Categorization

- Put the name of a machine/farm type into `machine_name.csv`.
- Put the name of a component used in a specific region into that region’s category CSV file.
- If a term applies to multiple categories and have the same meaning, include it in `general.csv`.
- If a term applies to multiple categories but has different meanings, include it in each relevant category CSV file with the appropriate definition for that context.
- `other.csv` is for terms that are not numerous enough to have their own category. Add new categories as needed.
