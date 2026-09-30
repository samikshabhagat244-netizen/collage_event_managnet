class RegistrationManager:
    """Handles event registration and cancellation in runtime memory."""

    def __init__(self):
        self.registrations = []

    def register(self, name, email, event_id, events):
        event = next((e for e in events if e["id"] == event_id), None)
        if event is None:
            return False

        count = sum(r["event_id"] == event_id for r in self.registrations)
        if count >= event["capacity"]:
            return False

        duplicate = any(
            r["name"].lower() == name.lower()
            and r["event_id"] == event_id
            for r in self.registrations
        )
        if duplicate:
            return False

        self.registrations.append({
            "name": name,
            "email": email,
            "event_id": event_id
        })
        return True

    def cancel(self, name, event_id):
        for registration in self.registrations:
            if (
                registration["name"].lower() == name.lower()
                and registration["event_id"] == event_id
            ):
                self.registrations.remove(registration)
                return True
        return False

    def registrations_for_event(self, event_id):
        return [r for r in self.registrations if r["event_id"] == event_id]
