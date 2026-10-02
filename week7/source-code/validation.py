# SmartCare v0.4 - shared input check used by Patient and Practitioner.


def require_text(value: str, field_name: str) -> str:
    """Return the text with spaces trimmed, or raise ValueError if it is empty."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError(field_name + " cannot be empty")
    return value.strip()
