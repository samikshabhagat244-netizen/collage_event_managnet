def validate_name(value):
    return bool(value and value.strip() and len(value.strip()) >= 2)

def validate_positive_int(value):
    try:
        return int(value) > 0
    except (ValueError, TypeError):
        return False

def validate_email(email):
    return isinstance(email, str) and "@" in email and "." in email
