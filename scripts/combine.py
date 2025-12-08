import argparse
import csv
import logging
import os

import config


def read_csv(path: str | os.PathLike) -> tuple[list[str], list[list[str]]]:
    with open(path, encoding=config.ENCODING) as f:
        reader = csv.reader(f)
        header = next(reader)  
        return header, [row for row in reader]


def main():
    contents = []
    template_header, _ = read_csv(config.TEMPLATE_PATH)
    for section in config.ORDER:
        header, rows = read_csv(config.GLOSSARY_DIR / f"{section}.csv")

        if header != template_header:
            logging.error(f"Header mismatch in {section}.csv")
            continue
        contents.extend(rows)

    with open(config.COMBINED_GLOSSARY_PATH, "w", encoding=config.ENCODING, newline='') as f:
        writer = csv.writer(f)
        writer.writerow(template_header)
        writer.writerows(contents)


def process_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Combine multiple glossary files into a single output file."
    )
    return parser.parse_args()

if __name__ == "__main__":
    # args = process_args()
    main()