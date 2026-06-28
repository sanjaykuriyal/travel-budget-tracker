# CLAUDE.md — Travel Budget Tracker

## Project Overview
A command-line Travel Budget Tracker written in Python.
Users can create trips, log expenses, and view budget summaries.
All data is saved to a local JSON file so it persists between runs.

## Coding Standards
- Use Python 3.10+
- Follow PEP 8 style guidelines
- Add a docstring to every function
- Use type hints for all function parameters and return values
- Keep functions small — one task per function
- Use f-strings for all string formatting (not .format() or % style)
- Never use global variables — pass data as function arguments

## Project Structure
```
travel_budget_tracker/
├── CLAUDE.md                  ← You are here (AI instruction file)
├── storage.py                 ← JSON file read/write functions
├── tracker.py                 ← Core business logic
├── display.py                 ← All print/display functions
├── main.py                    ← Menu entry point
└── tests/
    └── test_tracker.py        ← Unit tests
```

## Data Storage
- Save all data to a file called trips_data.json in the project root
- Data format: a list of trip objects
- Each trip object has: name (str), destination (str), budget (float), expenses (list)
- Each expense dict has: description (str), amount (float), date (str YYYY-MM-DD)

## Testing
- Use Python's built-in unittest module
- Name test files as test_<module_name>.py inside the tests/ folder
- Run tests with: python -m unittest discover
- Test all core functions: add_trip, add_expense, get_summary

## Off-Limits
- Do NOT modify CLAUDE.md unless explicitly asked
- Do NOT delete trips_data.json without user confirmation

## Notes for Claude Code
- Always read existing files before writing new ones
- Match the coding style of whatever file you are editing
- Explain what you are about to do before making any changes
