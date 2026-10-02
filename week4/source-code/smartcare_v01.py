# SmartCare v0.1 - Stage 1 Lab, Part B, task 1 enhanced
# Use lists, dictionaries and functions to enhance the Python file
# Includes the one Part G improvement (double-booking check) and the Part F tests.

appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")

    # Part G improvement: stop the same practitioner being booked twice at the same time
    for existing in appointments:
        if existing["practitioner"] == practitioner_name and existing["time"] == appointment_time:
            raise ValueError("This practitioner already has an appointment at that time")

    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")

print("Welcome to SmartCare: The Clinical Appointment Booking System!")
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')
display_appointments()


# ---------------------------------------------------------------
# Part F - Verify behaviour
# Each test tries one booking and prints whether it was accepted.
# ---------------------------------------------------------------

def try_booking(label, patient_name, practitioner_name, appointment_time):
    print(label)
    try:
        book_appointment(patient_name, practitioner_name, appointment_time)
        print("  Accepted")
    except Exception as error:
        print("  Rejected:", type(error).__name__, "-", error)

print()
print("Part F tests")
try_booking("Test 1: normal appointment", 'Cara Lee', 'Dr. Jane Roe', '2024-07-21 09:00 AM')
try_booking("Test 2: blank patient name", '', 'Dr. Jane Roe', '2024-07-21 10:00 AM')
try_booking("Test 3: same practitioner and time as Alice Smith", 'Dan Wu', 'Dr. John Doe', '2024-07-20 10:00 AM')
try_booking("Test 4: patient_name=None", None, 'Dr. Jane Roe', '2024-07-21 11:00 AM')
try_booking("Test 5: appointment_time=None", 'Eve Park', 'Dr. Jane Roe', None)

print()
print("Appointments after the tests")
display_appointments()
