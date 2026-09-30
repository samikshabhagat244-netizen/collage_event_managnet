class EventManager:
    """Manages college events in runtime memory only."""

    def __init__(self):
        self.events = [
            {
                "id": 1,
                "name": "CodeFest",
                "category": "Technical",
                "date": "15-10-2026",
                "capacity": 50
            },
            {
                "id": 2,
                "name": "Cultural Night",
                "category": "Cultural",
                "date": "20-10-2026",
                "capacity": 100
            },
            {
                "id": 3,
                "name": "Quiz Competition",
                "category": "Academic",
                "date": "25-10-2026",
                "capacity": 40
            }
        ]

    def show_events(self):
        for event in self.events:
            print(event)

    def add_event(self, name, category, date, capacity):
        new_id = max((e["id"] for e in self.events), default=0) + 1
        self.events.append({
            "id": new_id,
            "name": name,
            "category": category,
            "date": date,
            "capacity": capacity
        })

    def search_events(self, keyword):
        keyword = keyword.lower()
        return [
            event for event in self.events
            if keyword in event["name"].lower()
            or keyword in event["category"].lower()
        ]

    def get_event(self, event_id):
        for event in self.events:
            if event["id"] == event_id:
                return event
        return None
