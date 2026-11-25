def display_session_report(sessions, registrations, feedback):
    """Print registration, attendance and feedback statistics."""
    try:
        session_id = int(input("Enter session ID for report: "))
    except ValueError:
        print("Session ID must be a whole number.")
        return

    if session_id not in sessions:
        print("Session not found.")
        return

    details = sessions[session_id]
    registered_ids = registrations.get(session_id, [])
    attended_ids = details.get("attended", [])
    feedback_entries = feedback.get(session_id, [])

    registered_count = len(registered_ids)
    attended_count = len(attended_ids)

    if registered_count > 0:
        attendance_percentage = attended_count / registered_count * 100
    else:
        attendance_percentage = 0

    if feedback_entries:
        average_rating = sum(item["rating"] for item in feedback_entries) / len(feedback_entries)
    else:
        average_rating = 0

    print("\n--- Session Report ---")
    print(f"Session: {details['title']}")
    print(f"Venue capacity: {details['capacity']}")
    print(f"Registered: {registered_count}")
    print(f"Attended: {attended_count}")
    print(f"Attendance percentage: {attendance_percentage:.1f}%")
    print(f"Feedback received: {len(feedback_entries)}")

    if feedback_entries:
        print(f"Average feedback rating: {average_rating:.1f}/5")
        print("Comments:")
        for item in feedback_entries:
            print(f"- {item['comment']}")
    else:
        print("No feedback has been submitted yet.")
