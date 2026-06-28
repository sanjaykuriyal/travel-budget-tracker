import json
from pathlib import Path
from typing import Any

DATA_FILE = Path(__file__).resolve().parent / "trips_data.json"


def load_trips(file_path: Path = DATA_FILE) -> list[dict[str, Any]]:
    """Load trips from the JSON data file and return them as a list."""
    if not file_path.exists():
        return []

    with file_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def save_trips(trips: list[dict[str, Any]], file_path: Path = DATA_FILE) -> None:
    """Save the trips list to the JSON data file."""
    with file_path.open("w", encoding="utf-8") as handle:
        json.dump(trips, handle, indent=2)
