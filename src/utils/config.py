import json
from pathlib import Path

# Loading config data

PATH = Path(__file__).resolve().parents[2]

with open(PATH / "src/_setup/config.json") as f:
    config = json.load(f)

# Change config.json

