# SmartCare v0.4 - Stage 4 Lab, Part C
# Practitioner domain class with identifier, name and specialty. (FR-04)
# No database logic: the class only holds and protects its own data.

from validation import require_text


class Practitioner:
    """A practitioner who patients book appointments with."""

    def __init__(self, practitioner_id: str, name: str, specialty: str) -> None:
        self._practitioner_id = require_text(practitioner_id, "Practitioner ID")
        self._name = require_text(name, "Practitioner name")
        self._specialty = require_text(specialty, "Practitioner specialty")

    @property
    def practitioner_id(self) -> str:
        return self._practitioner_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def specialty(self) -> str:
        return self._specialty

    def __repr__(self) -> str:
        return f"Practitioner({self._practitioner_id}, {self._name}, {self._specialty})"
