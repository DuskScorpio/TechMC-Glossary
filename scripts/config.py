from pathlib import Path

ENCODING = "utf-8-sig"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = PROJECT_ROOT / "scripts"
GLOSSARY_DIR = PROJECT_ROOT / "categories"
LOG_DIR = PROJECT_ROOT / "logs"

COMBINED_GLOSSARY_PATH = PROJECT_ROOT / "TechMC Glossary.csv"
TEMPLATE_PATH = GLOSSARY_DIR / "_template.csv"

ORDER = [
    "general",
    "machine_name",
    "storage",
    "slimestone",
    "mechanical",
    "tree_farm",
    "mob_farm",
    "glitch",
    "coding",
    "science",
    "computational",
    "1.12.2_magic",
    "other",
]
