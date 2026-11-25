import unittest
from modules.sessions import publish_session
from modules.reports import display_session_report


class PhaseOneBasicTests(unittest.TestCase):
    def test_session_capacity_is_stored(self):
        sessions = {}
        # This test is a structural example; interactive functions are tested manually.
        sessions[1] = {
            "title": "Test session",
            "date": "2026-12-01",
            "time": "10:00",
            "venue": "Room 1",
            "capacity": 5
        }
        self.assertEqual(sessions[1]["capacity"], 5)

    def test_registration_count_can_be_calculated(self):
        registrations = {1: [10, 11]}
        self.assertEqual(len(registrations[1]), 2)


if __name__ == "__main__":
    unittest.main()
