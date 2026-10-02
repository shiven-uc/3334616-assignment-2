# SmartCare v0.3 - Stage 3 Lab, Part H
# Consistency check: does the code have every class, attribute and operation
# that is drawn in the UML class diagram?

from datetime import datetime
from smartcare_v03 import AppointmentStatus, Patient, Practitioner, Appointment, Clinic

results = []

def check(description, condition):
    results.append(condition)
    if condition:
        print("OK   ", description)
    else:
        print("FAIL ", description)

patient = Patient("P001", "Alice Smith", "0400 000 001")
practitioner = Practitioner("D01", "Dr. John Doe")
appointment = Appointment("A001", patient, practitioner, datetime(2024, 7, 20, 10, 0))
clinic = Clinic()

print("Patient")
for name in ["patient_id", "name", "phone", "matches_name"]:
    check("Patient has " + name, hasattr(patient, name))

print("Practitioner")
for name in ["practitioner_id", "name"]:
    check("Practitioner has " + name, hasattr(practitioner, name))

print("Appointment")
for name in ["appointment_id", "patient", "practitioner", "date_time", "status", "cancel", "is_booked"]:
    check("Appointment has " + name, hasattr(appointment, name))
check("Appointment.patient is a Patient", isinstance(appointment.patient, Patient))
check("Appointment.practitioner is a Practitioner", isinstance(appointment.practitioner, Practitioner))
check("A new appointment has status Booked", appointment.status == AppointmentStatus.BOOKED)

print("AppointmentStatus")
check("AppointmentStatus has exactly Booked, Cancelled, Completed",
      [status.value for status in AppointmentStatus] == ["Booked", "Cancelled", "Completed"])

print("Clinic")
for name in ["patients", "practitioners", "appointments", "register_patient", "add_practitioner",
             "find_patient_by_id", "find_patients_by_name", "book_appointment",
             "appointments_for_practitioner", "appointments_for_patient"]:
    check("Clinic has " + name, hasattr(clinic, name))

print()
print(results.count(True), "of", len(results), "checks passed")
