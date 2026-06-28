# Travel Budget Tracker

A command-line Travel Budget Tracker written in Python. Create trips, log
expenses, and view budget summaries. All data is saved to a local JSON file so
it persists between runs.

## Requirements

- Python 3.10+

## Usage

```bash
python main.py
```

You'll get a menu to:

1. Add a trip
2. Add an expense
3. View a trip summary
4. List trips
5. Exit

## Project Structure

```
travel-budget-tracker/
├── storage.py            # JSON file read/write functions
├── tracker.py            # Core business logic
├── display.py            # All print/display functions
├── main.py               # Menu entry point
└── tests/
    └── test_tracker.py   # Unit tests
```

## Running Tests

```bash
python -m unittest discover
```
