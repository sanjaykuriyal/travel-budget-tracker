from typing import Any


def create_trip(trips: list[dict[str, Any]], name: str, destination: str, budget: float) -> dict[str, Any]:
    """Create a new trip and append it to the trips list."""
    trip = {
        "name": name,
        "destination": destination,
        "budget": budget,
        "expenses": [],
    }
    trips.append(trip)
    return trip


def find_trip(trips: list[dict[str, Any]], trip_name: str) -> dict[str, Any] | None:
    """Find a trip by name and return it, or None when not found."""
    normalized_name = trip_name.strip().lower()
    for trip in trips:
        if trip["name"].strip().lower() == normalized_name:
            return trip
    return None


def add_expense(
    trips: list[dict[str, Any]],
    trip_name: str,
    description: str,
    amount: float,
    date: str,
) -> bool:
    """Add an expense to the specified trip. Return True when successful."""
    trip = find_trip(trips, trip_name)
    if trip is None:
        return False

    expense = {
        "description": description,
        "amount": amount,
        "date": date,
    }
    trip["expenses"].append(expense)
    return True


def get_summary(trips: list[dict[str, Any]], trip_name: str) -> dict[str, Any]:
    """Return a summary for the named trip, including total spent and remaining budget."""
    trip = find_trip(trips, trip_name)
    if trip is None:
        raise ValueError(f"Trip not found: {trip_name}")

    total_spent = sum(expense["amount"] for expense in trip["expenses"])
    return {
        "name": trip["name"],
        "destination": trip["destination"],
        "budget": trip["budget"],
        "total_spent": total_spent,
        "remaining": trip["budget"] - total_spent,
        "expenses": trip["expenses"],
    }


def list_trip_names(trips: list[dict[str, Any]]) -> list[str]:
    """Return a list of trip names from the trips list."""
    return [trip["name"] for trip in trips]
