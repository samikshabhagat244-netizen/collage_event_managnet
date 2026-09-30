from event_manager import EventManager
from participant_manager import ParticipantManager
from registration_manager import RegistrationManager
from validation import validate_name, validate_positive_int, validate_email

def test_event_search():
    manager = EventManager()
    result = manager.search_events("Code")
    assert len(result) == 1

def test_add_event():
    manager = EventManager()
    before = len(manager.events)
    manager.add_event("Sports Day", "Sports", "30-10-2026", 30)
    assert len(manager.events) == before + 1

def test_registration():
    events = EventManager()
    registrations = RegistrationManager()
    assert registrations.register("Aarav", "aarav@example.com", 1, events.events)
    assert len(registrations.registrations) == 1

def test_duplicate_registration():
    events = EventManager()
    registrations = RegistrationManager()
    registrations.register("Aarav", "aarav@example.com", 1, events.events)
    assert not registrations.register("Aarav", "aarav@example.com", 1, events.events)

def test_cancellation():
    events = EventManager()
    registrations = RegistrationManager()
    registrations.register("Aarav", "aarav@example.com", 1, events.events)
    assert registrations.cancel("Aarav", 1)
    assert len(registrations.registrations) == 0

def test_validation():
    assert validate_name("Aarav")
    assert validate_positive_int("10")
    assert validate_email("student@example.com")

if __name__ == "__main__":
    test_event_search()
    test_add_event()
    test_registration()
    test_duplicate_registration()
    test_cancellation()
    test_validation()
    print("All tests passed successfully.")
