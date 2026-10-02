# SmartCare v0.4 - Stage 4 Lab, Part F
# Manual behaviour checks for Patient, Practitioner and Appointment.
# Each check says what should happen and prints OK or FAIL.

from datetime import datetime

from patient import Patient
from practitioner import Practitioner
from appointment import Appointment, AppointmentStatus, InvalidStatusTransitionError

results = []


def check(description, condition):
    results.append(condition)
    if condition:
        print("OK   ", description)
    else:
        print("FAIL ", description)


def raises(expected_error, action):
    """Return True if running the action raises the expected error."""
    try:
        action()
    except expected_error:
        return True
    except Exception:
        return False
    return False


print("1. Create valid objects")
patient = Patient("P001", "Alice Smith", "0400 000 001")
practitioner = Practitioner("D01", "Dr. John Doe", "General Practice")
appointment = Appointment("A001", patient, practitioner, datetime(2024, 7, 20, 10, 0))
print("  ", patient)
print("  ", practitioner)
print("  ", appointment)
check("Patient keeps its ID, name and phone",
      patient.patient_id == "P001" and patient.name == "Alice Smith" and patient.phone == "0400 000 001")
check("Practitioner keeps its ID, name and specialty",
      practitioner.practitioner_id == "D01" and practitioner.specialty == "General Practice")
check("Appointment is linked to its Patient and Practitioner",
      appointment.patient is patient and appointment.practitioner is practitioner)
check("A new appointment starts as Booked", appointment.status == AppointmentStatus.BOOKED)
check("matches_name finds 'alice' in Alice Smith", patient.matches_name("alice"))
check("matches_name does not find 'bob'", not patient.matches_name("bob"))

print()
print("2. Invalid input")
check("Blank patient name is rejected",
      raises(ValueError, lambda: Patient("P002", "", "0400 000 002")))
check("Patient name of one space is rejected",
      raises(ValueError, lambda: Patient("P002", " ", "0400 000 002")))
check("Patient name of None is rejected",
      raises(ValueError, lambda: Patient("P002", None, "0400 000 002")))
check("Blank patient ID is rejected",
      raises(ValueError, lambda: Patient("", "Bob Johnson", "0400 000 002")))
check("Blank practitioner specialty is rejected",
      raises(ValueError, lambda: Practitioner("D02", "Dr. Jane Roe", "")))
check("Appointment with a name instead of a Patient is rejected",
      raises(TypeError, lambda: Appointment("A002", "Alice Smith", practitioner, datetime(2024, 7, 20, 11, 0))))
check("Appointment with text instead of a date and time is rejected",
      raises(TypeError, lambda: Appointment("A002", patient, practitioner, "2024-07-20 11:00 AM")))
check("Appointment with a date and time of None is rejected",
      raises(TypeError, lambda: Appointment("A002", patient, practitioner, None)))

print()
print("3. Protected state")
check("Status cannot be set directly from outside",
      raises(AttributeError, lambda: setattr(appointment, "status", AppointmentStatus.COMPLETED)))
check("Patient name cannot be set directly from outside",
      raises(AttributeError, lambda: setattr(patient, "name", "Someone Else")))

print()
print("4. Cancel a booked appointment")
appointment.cancel()
print("  ", appointment)
check("Status is now Cancelled", appointment.status == AppointmentStatus.CANCELLED)
check("is_booked is now False", not appointment.is_booked())
check("The cancelled appointment still exists with its patient", appointment.patient is patient)

print()
print("5. Illegal repeated transitions")
check("Cancelling a cancelled appointment is rejected",
      raises(InvalidStatusTransitionError, appointment.cancel))
check("Completing a cancelled appointment is rejected",
      raises(InvalidStatusTransitionError, appointment.complete))
check("Status is still Cancelled afterwards", appointment.status == AppointmentStatus.CANCELLED)

second = Appointment("A003", patient, practitioner, datetime(2024, 7, 21, 9, 0))
second.complete()
check("A booked appointment can be completed", second.status == AppointmentStatus.COMPLETED)
check("Cancelling a completed appointment is rejected",
      raises(InvalidStatusTransitionError, second.cancel))

print()
print(results.count(True), "of", len(results), "checks passed")
