from typing import Any


def print_menu() -> None:
    """Print the command-line menu options."""
    print("\nTravel Budget Tracker")
    print("1. Add a trip")
    print("2. Add an expense")
    print("3. View trip summary")
    print("4. List trips")
    print("5. Exit")


def print_trips(trips: list[dict[str, Any]]) -> None:
    """Print the list of trips."""
    if not trips:
        print("No trips found.")
        return

    print("\nSaved trips:")
    for index, trip in enumerate(trips, start=1):
        print(
            f"{index}. {trip['name']} — {trip['destination']} (Budget: {trip['budget']:.2f})"
        )


def print_summary(summary: dict[str, Any]) -> None:
    """Print the summary of a trip."""
    print(f"\nSummary for {summary['name']} ({summary['destination']}):")
    print(f"Budget: {summary['budget']:.2f}")
    print(f"Total spent: {summary['total_spent']:.2f}")
    print(f"Remaining: {summary['remaining']:.2f}")
    if summary["expenses"]:
        print("\nExpenses:")
        for expense in summary["expenses"]:
            print(
                f"- {expense['date']}: {expense['description']} — {expense['amount']:.2f}"
            )
    else:
        print("No expenses recorded yet.")


def print_message(message: str) -> None:
    """Print a generic message to the user."""
    print(message)
