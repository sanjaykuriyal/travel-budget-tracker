from pathlib import Path

from display import print_menu, print_message, print_summary, print_trips
from storage import load_trips, save_trips
from tracker import add_expense, create_trip, get_summary, list_trip_names, find_trip


def get_float(prompt: str) -> float:
    """Prompt the user for a float value."""
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number.")


def main() -> None:
    """Run the Travel Budget Tracker command-line loop."""
    data_path = Path(__file__).resolve().parent / "trips_data.json"
    trips = load_trips(data_path)

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Trip name: ").strip()
            destination = input("Destination: ").strip()
            budget = get_float("Budget amount: ")
            create_trip(trips, name, destination, budget)
            save_trips(trips, data_path)
            print_message("Trip added successfully.")

        elif choice == "2":
            if not trips:
                print_message("No trips available. Add a trip first.")
                continue

            trip_name = input("Trip name: ").strip()
            if find_trip(trips, trip_name) is None:
                print_message("Trip not found. Please enter an existing trip name.")
                continue

            description = input("Expense description: ").strip()
            amount = get_float("Expense amount: ")
            date = input("Expense date (YYYY-MM-DD): ").strip()
            added = add_expense(trips, trip_name, description, amount, date)
            if added:
                save_trips(trips, data_path)
                print_message("Expense added successfully.")
            else:
                print_message("Failed to add expense.")

        elif choice == "3":
            if not trips:
                print_message("No trips available.")
                continue

            trip_name = input("Trip name: ").strip()
            try:
                summary = get_summary(trips, trip_name)
                print_summary(summary)
            except ValueError:
                print_message("Trip not found. Please enter an existing trip name.")

        elif choice == "4":
            print_trips(trips)

        elif choice == "5":
            print_message("Goodbye!")
            break

        else:
            print_message("Please select a valid option.")


if __name__ == "__main__":
    main()
