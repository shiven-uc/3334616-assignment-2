# SmartCare v0.3 - Stage 3 Lab, Part G
# Class skeletons for the domain model in the Domain Model Workbook.
# The classes store their data, but the behaviour is not implemented yet.
# Each method says which requirement it supports and will be written in Stage 4.

from datetime import datetime
from enum import Enum


class AppointmentStatus(Enum):
    """The only statuses an appointment can have. (FR-09, BR-05)"""
    BOOKED = "Booked"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"


class Patient:
    """A person registered at the clinic. (FR-01)"""

    def __init__(self, patient_id, name, phone):
        self.patient_id = patient_id
        self.name = name
        self.phone = phone

    def matches_name(self, text):
        """Return True if this patient's name contains the search text. (FR-03)"""
        pass


class Practitioner:
    """A GP who patients book appointments with. (FR-04)"""

    def __init__(self, practitioner_id, name):
        self.practitioner_id = practitioner_id
        self.name = name


class Appointment:
    """One booking for one patient with one practitioner. (FR-05, BR-02)"""

    def __init__(self, appointment_id, patient, practitioner, date_time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date_time = date_time
        self.status = AppointmentStatus.BOOKED

    def cancel(self):
        """Change the status to Cancelled. The appointment is kept. (FR-07, BR-04)"""
        pass

    def is_booked(self):
        """Return True if the status is Booked, so it blocks its time slot. (BR-01)"""
        pass


class Clinic:
    """Holds the lists and checks the rules that need every record. (BR-01, BR-03)"""

    def __init__(self):
        self.patients = []
        self.practitioners = []
        self.appointments = []

    def register_patient(self, patient_id, name, phone):
        """Create a patient with a unique ID and add it to the list. (FR-01, BR-03)"""
        pass

    def add_practitioner(self, practitioner_id, name):
        """Create a practitioner with a unique ID and add it to the list. (FR-04, BR-03)"""
        pass

    def find_patient_by_id(self, patient_id):
        """Return the patient with this ID. (FR-02)"""
        pass

    def find_patients_by_name(self, text):
        """Return every patient whose name matches. (FR-03)"""
        pass

    def book_appointment(self, patient, practitioner, date_time):
        """Create an appointment unless the practitioner is already booked. (FR-05, FR-06, BR-01)"""
        pass

    def appointments_for_practitioner(self, practitioner, date):
        """Return a practitioner's appointments for one date, in time order. (FR-10)"""
        pass

    def appointments_for_patient(self, patient):
        """Return a patient's appointments, including cancelled ones. (FR-11)"""
        pass


if __name__ == "__main__":
    # Small demonstration that the skeletons can be created and linked together.
    clinic = Clinic()
    patient = Patient("P001", "Alice Smith", "0400 000 001")
    practitioner = Practitioner("D01", "Dr. John Doe")
    appointment = Appointment("A001", patient, practitioner, datetime(2024, 7, 20, 10, 0))

    print("SmartCare v0.3 class skeletons")
    print("Patient:", patient.patient_id, patient.name, patient.phone)
    print("Practitioner:", practitioner.practitioner_id, practitioner.name)
    print("Appointment:", appointment.appointment_id, "|", appointment.patient.name, "|",
          appointment.practitioner.name, "|", appointment.date_time, "|", appointment.status.value)
    print("Clinic lists:", len(clinic.patients), "patients,", len(clinic.practitioners),
          "practitioners,", len(clinic.appointments), "appointments")
