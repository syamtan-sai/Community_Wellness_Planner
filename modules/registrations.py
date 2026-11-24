def register_participant(sessions, participants, registrations):
    """Register a known participant if the session has available capacity."""
    try:
        session_id = int(input("Enter session ID: "))
        participant_id = int(input("Enter participant ID: "))
    except ValueError:
        print("IDs must be whole numbers.")
        return

    if session_id not in sessions:
        print("Session not found.")
        return

    if participant_id not in participants:
        print("Participant not found in sample participant records.")
        return

    registered_ids = registrations.setdefault(session_id, [])

    if participant_id in registered_ids:
        print("This participant is already registered for the session.")
        return

    capacity = sessions[session_id]["capacity"]
    if len(registered_ids) >= capacity:
        print("Registration is full. Venue capacity has been reached.")
        return

    registered_ids.append(participant_id)
    print(f"{participants[participant_id]} registered successfully.")


def mark_attendance(sessions, registrations):
    """Record attendance for a registered participant."""
    try:
        session_id = int(input("Enter session ID: "))
        participant_id = int(input("Enter participant ID: "))
    except ValueError:
        print("IDs must be whole numbers.")
        return

    if session_id not in sessions:
        print("Session not found.")
        return

    if participant_id not in registrations.get(session_id, []):
        print("Participant is not registered for this session.")
        return

    sessions[session_id].setdefault("attended", [])
    attended_ids = sessions[session_id]["attended"]

    if participant_id in attended_ids:
        print("Attendance has already been recorded.")
        return

    attended_ids.append(participant_id)
    print("Attendance marked.")


def submit_feedback(sessions, registrations, feedback):
    """Store a rating and a comment from a registered participant."""
    try:
        session_id = int(input("Enter session ID: "))
        participant_id = int(input("Enter participant ID: "))
        rating = int(input("Rating (1-5): "))
    except ValueError:
        print("Session ID, participant ID and rating must be whole numbers.")
        return

    if session_id not in sessions:
        print("Session not found.")
        return

    if participant_id not in registrations.get(session_id, []):
        print("Only registered participants can submit feedback.")
        return

    if rating < 1 or rating > 5:
        print("Rating must be between 1 and 5.")
        return

    entries = feedback.setdefault(session_id, [])
    if any(entry["participant_id"] == participant_id for entry in entries):
        print("Feedback has already been submitted by this participant.")
        return

    comment = input("Comment (enter None if you have no comment): ").strip()
    if not comment:
        comment = "None"

    entries.append({
        "participant_id": participant_id,
        "rating": rating,
        "comment": comment
    })
    print("Feedback submitted.")
