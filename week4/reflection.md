# Reflection - Stage 1 Lab (Week 4)

Before using AI, my starting point was the two programs in the lab handout. The first stores two appointments in separate variables and prints them. The second keeps appointments as dictionaries in a list and has two functions, `book_appointment` and `display_appointments`, with a check that the patient name is not empty.

The AI tutor helped me understand why `if not patient_name` catches both an empty string and `None`, and it pointed out limitations such as the time being plain text and nothing stopping a double booking.

The AI did make assumptions when it wrote its own version. It called `.strip()` on every value, which assumes every input is text, and it returned the appointment even though that was not requested. It did not validate anything.

I verified the AI output by running both versions with the same five inputs. The AI version accepted a blank patient name and a duplicate booking, and crashed with an `AttributeError` when a value was `None`. The handout version rejected the blank and `None` patient names.

The engineering work that remained was deciding what SmartCare actually needs. I chose one improvement, a double-booking check, because duplicate bookings are a problem the clinic reported, and I tested that it works. Ideas like saving to a database were left out because they are outside Stage 1.
