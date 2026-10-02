# SmartCare v0.4 - Stage 4 Lab, Parts D to G
# Appointment domain class, after the AI-generated version was reviewed and refactored.
# (FR-05, FR-07, FR-08, FR-09, BR-02, BR-04, BR-05)

from datetime import datetime
from enum import Enum

from patient import Patient
from practitioner import Practitioner
from validation import require_text


class AppointmentStatus(Enum):
    """The only statuses an appointment can have. (FR-09, BR-05)"""
    BOOKED = "Booked"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"


class InvalidStatusTransitionError(Exception):
    """Raised when an appointment is asked to make a status change that is not allowed."""


class Appointment:
    """One booking for one patient with one practitioner. (BR-02)"""

    def __init__(self, appointment_id: str, patient: Patient, practitioner: Practitioner,
                 date_time: datetime) -> None:
        if not isinstance(patient, Patient):
            raise TypeError("patient must be a Patient")
        if not isinstance(practitioner, Practitioner):
            raise TypeError("practitioner must be a Practitioner")
        if not isinstance(date_time, datetime):
            raise TypeError("date_time must be a datetime")
        self._appointment_id = require_text(appointment_id, "Appointment ID")
        self._patient = patient
        self._practitioner = practitioner
        self._date_time = date_time
        # A new appointment always starts as Booked. (FR-05)
        self._status = AppointmentStatus.BOOKED

    @property
    def appointment_id(self) -> str:
        return self._appointment_id

    @property
    def patient(self) -> Patient:
        return self._patient

    @property
    def practitioner(self) -> Practitioner:
        return self._practitioner

    @property
    def date_time(self) -> datetime:
        return self._date_time

    @property
    def status(self) -> AppointmentStatus:
        return self._status

    def is_booked(self) -> bool:
        """Return True if the status is Booked, so it blocks its time slot. (BR-01)"""
        return self._status == AppointmentStatus.BOOKED

    def cancel(self) -> None:
        """Change Booked to Cancelled. The appointment object is kept. (FR-07, BR-04)"""
        if self._status != AppointmentStatus.BOOKED:
            raise InvalidStatusTransitionError(
                "Cannot cancel an appointment that is " + self._status.value)
        self._status = AppointmentStatus.CANCELLED

    def complete(self) -> None:
        """Change Booked to Completed. (FR-09)"""
        if self._status != AppointmentStatus.BOOKED:
            raise InvalidStatusTransitionError(
                "Cannot complete an appointment that is " + self._status.value)
        self._status = AppointmentStatus.COMPLETED

    def __repr__(self) -> str:
        return (f"Appointment({self._appointment_id}, {self._patient.name}, "
                f"{self._practitioner.name}, {self._date_time}, {self._status.value})")
