# Sample data for demonstration. No external or institutional records are used.

sessions = {
    101: {
        "title": "Stress Management",
        "date": "2026-12-05",
        "time": "10:00 AM",
        "venue": "Seminar Hall A",
        "capacity": 3
    },
    102: {
        "title": "Yoga and Mindfulness",
        "date": "2026-12-08",
        "time": "3:00 PM",
        "venue": "Wellness Room",
        "capacity": 2
    }
}

# Participant IDs map to participant names.
participants = {
    1: "Aarav",
    2: "Diya",
    3: "Kabir",
    4: "Meera"
}

# Each session ID maps to a list of participant IDs.
registrations = {
    101: [1],
    102: []
}

# Each session ID maps to feedback entries.
feedback = {
    101: [],
    102: []
}
