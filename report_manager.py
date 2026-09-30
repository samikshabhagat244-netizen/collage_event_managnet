class ReportManager:
    """Creates reports from current runtime objects."""

    def __init__(self, event_manager, participant_manager, registration_manager):
        self.events = event_manager
        self.participants = participant_manager
        self.registrations = registration_manager

    def show_report(self):
        print("\n===== REGISTRATION REPORT =====")
        print("Total events:", len(self.events.events))
        print("Participants stored in session:", len(self.participants.participants))
        print("Total registrations:", len(self.registrations.registrations))

        print("\nRegistrations by event:")
        for event in self.events.events:
            count = len(self.registrations.registrations_for_event(event["id"]))
            print(f"{event['name']} (ID {event['id']}): {count}/{event['capacity']}")

        print("\nData policy: runtime memory only; no database/file persistence.")
