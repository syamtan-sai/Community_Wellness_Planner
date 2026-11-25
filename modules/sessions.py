def publish_session(sessions):
    """Collect session details and add a new session."""
    title = input("Session title: ").strip()
    date = input("Date (YYYY-MM-DD): ").strip()
    time = input("Time: ").strip()
    venue = input("Venue: ").strip()

    try:
        capacity = int(input("Venue capacity: "))
    except ValueError:
        print("Capacity must be a whole number.")
        return

    if not title or not date or not time or not venue or capacity <= 0:
        print("Please enter all details and a positive capacity.")
        return

    if sessions:
        session_id = max(sessions) + 1
    else:
        session_id = 101

    sessions[session_id] = {
        "title": title,
        "date": date,
        "time": time,
        "venue": venue,
        "capacity": capacity
    }

    print(f"Session published. Session ID: {session_id}")


def display_sessions(sessions):
    """Display all published sessions."""
    if not sessions:
        print("No sessions have been published.")
        return

    print("\n--- Published Sessions ---")
    for session_id, details in sessions.items():
        print(
            f"ID: {session_id} | {details['title']} | "
            f"{details['date']} at {details['time']} | "
            f"Venue: {details['venue']} | Capacity: {details['capacity']}"
        )
