from data.sample_data import sessions, participants, registrations, feedback
from modules.sessions import publish_session, display_sessions
from modules.registrations import register_participant, mark_attendance, submit_feedback
from modules.reports import display_session_report


def display_menu():
    """Display the main menu."""
    print("\n=== Community Wellness Session Planner ===")
    print("1. Publish a wellness session")
    print("2. View sessions")
    print("3. Register for a session")
    print("4. Mark attendance")
    print("5. Submit participant feedback")
    print("6. View session report")
    print("0. Exit")


def main():
    """Run the menu-driven application."""
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            publish_session(sessions)
        elif choice == "2":
            display_sessions(sessions)
        elif choice == "3":
            register_participant(sessions, participants, registrations)
        elif choice == "4":
            mark_attendance(sessions, registrations)
        elif choice == "5":
            submit_feedback(sessions, registrations, feedback)
        elif choice == "6":
            display_session_report(sessions, registrations, feedback)
        elif choice == "0":
            print("Exiting the planner.")
            break
        else:
            print("Invalid choice. Please select an option from the menu.")


if __name__ == "__main__":
    main()
