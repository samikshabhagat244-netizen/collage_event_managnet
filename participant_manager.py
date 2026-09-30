class ParticipantManager:
    """Maintains participants for the current program session."""

    def __init__(self):
        self.participants = []

    def add_participant(self, name, email):
        participant = {"name": name, "email": email}
        if participant not in self.participants:
            self.participants.append(participant)

    def show_participants(self):
        if not self.participants:
            print("No participants recorded in this session.")
            return
        for participant in self.participants:
            print(participant)
