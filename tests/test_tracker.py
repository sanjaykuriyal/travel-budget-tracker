import unittest

from tracker import add_expense, create_trip, get_summary, list_trip_names


class TrackerTests(unittest.TestCase):
    def test_create_trip(self) -> None:
        trips = []
        trip = create_trip(trips, "Weekend", "Paris", 1200.0)

        self.assertEqual(len(trips), 1)
        self.assertEqual(trip["name"], "Weekend")
        self.assertEqual(trip["destination"], "Paris")
        self.assertEqual(trip["budget"], 1200.0)
        self.assertEqual(trip["expenses"], [])

    def test_add_expense(self) -> None:
        trips = []
        create_trip(trips, "City Break", "Tokyo", 2300.0)
        result = add_expense(trips, "City Break", "Dinner", 45.0, "2026-07-01")

        self.assertTrue(result)
        self.assertEqual(len(trips[0]["expenses"]), 1)
        self.assertEqual(trips[0]["expenses"][0]["description"], "Dinner")

    def test_get_summary(self) -> None:
        trips = []
        create_trip(trips, "Road Trip", "California", 1800.0)
        add_expense(trips, "Road Trip", "Fuel", 120.0, "2026-07-05")
        add_expense(trips, "Road Trip", "Hotel", 450.0, "2026-07-06")

        summary = get_summary(trips, "Road Trip")

        self.assertEqual(summary["total_spent"], 570.0)
        self.assertEqual(summary["remaining"], 1230.0)
        self.assertEqual(summary["name"], "Road Trip")

    def test_list_trip_names(self) -> None:
        trips = []
        create_trip(trips, "Beach", "Miami", 900.0)
        create_trip(trips, "Mountain", "Denver", 1100.0)

        self.assertEqual(list_trip_names(trips), ["Beach", "Mountain"])


if __name__ == "__main__":
    unittest.main()
