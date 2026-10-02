# SmartCare v0.4 - Stage 4 Lab, Part B
# Patient domain class with type hints and basic validation. (FR-01, FR-03)

from validation import require_text


class Patient:
    """A person registered at the clinic."""

    def __init__(self, patient_id: str, name: str, phone: str) -> None:
        self._patient_id = require_text(patient_id, "Patient ID")
        self._name = require_text(name, "Patient name")
        self._phone = require_text(phone, "Patient phone")

    @property
    def patient_id(self) -> str:
        return self._patient_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def phone(self) -> str:
        return self._phone

    def matches_name(self, text: str) -> bool:
        """Return True if this patient's name contains the search text. (FR-03)"""
        search = text.strip().lower()
        if not search:
            return False
        return search in self._name.lower()

    def __repr__(self) -> str:
        return f"Patient({self._patient_id}, {self._name}, {self._phone})"
