
from event_manager import EventManager
from participant_manager import ParticipantManager
from registration_manager import RegistrationManager
from report_manager import ReportManager
from validation import validate_name, validate_positive_int
def main():
    events = EventManager()
    participants = ParticipantManager()
    registrations = RegistrationManager()
    reports = ReportManager(events, participants, registrations)
    while True:
        print("\n===== COLLEGE EVENT REGISTRATION SYSTEM =====")
        print("1. View Events")
        print("2. Add Event")
        print("3. Search Event")
        print("4. Register Participant")
        print("5. View Participants")
        print("6. Cancel Registration")
        print("7. View Registration Report")
        print("8. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            events.show_events()
        elif choice == "2":
            name = input("Event name: ")
            category = input("Category: ")
            date = input("Date (DD-MM-YYYY): ")
            capacity = input("Capacity: ")
            if validate_name(name) and validate_name(category) and validate_positive_int(capacity):
                events.add_event(name, category, date, int(capacity))
                print("Event added successfully.")
            else:
                print("Invalid event details.")
        elif choice == "3":
            keyword = input("Search keyword: ")
            results = events.search_events(keyword)
            if results:
                for event in results:
                    print(event)
            else:
                print("No matching event found.")
        elif choice == "4":
            participant = input("Participant name: ")
            email = input("Email: ")
            event_id = input("Event ID: ")
            if not validate_name(participant):
                print("Invalid participant name.")
                continue
            if not validate_positive_int(event_id):
                print("Invalid event ID.")
                continue
            if registrations.register(
                participant,
                email,
                int(event_id),
                events.events
            ):
                print("Registration successful.")
            else:
                print("Registration failed. Check event ID or capacity.")
        elif choice == "5":
            participants.show_participants()
        elif choice == "6":
            participant = input("Participant name: ")
            event_id = input("Event ID: ")
            if validate_positive_int(event_id):
                if registrations.cancel(participant, int(event_id)):
                    print("Registration cancelled.")
                else:
                    print("Registration not found.")
        elif choice == "7":
            reports.show_report()
        elif choice == "8":
            print("Thank you. Program ended.")
            print("All runtime data has been cleared.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
