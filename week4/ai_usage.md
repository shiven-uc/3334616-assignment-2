# AI Usage - Week 4 (Stage 1)

- **Tool used:** ChatGPT
- **Note on the tool:** the lab handout names UC-approved tools such as Microsoft Copilot. I used Claude instead and am declaring that here.


## What the AI did

| Item | AI contribution |
| --- | --- |
| Tutorial handout | Drafted the answers to Activities 1 to 4 and the exit question. |
| Initial Engineering Brief | Drafted sections 1 to 5. |
| AI Activity Card | Acted as the AI tutor, and drafted the card from its own suggestions and test runs. |
| Lab Parts A and B | Drafted the answers and the list of limitations. |
| Lab Part C | Answered the tutor prompt: explained the code, gave three limitations, suggested improvements and asked two questions. |
| Lab Part D | Generated the alternative function in `source-code/smartcare_ai_version.py`. |
| Lab Parts E and F | Wrote the `try_booking` test helper, ran both versions with the five test inputs and drafted the comparison table. |
| Lab Part G | Wrote the double-booking check added to `source-code/smartcare_v01.py`. |
| Lab Part H | Drafted the reflection. |
| Git and GitHub | Explained the setup commands. I typed and ran them myself. |

## Prompts used

**Part C (tutor prompt, from the handout):**

> Act as a Python tutor. I am learning introductory software technology. Here is a small appointment-booking function. 1. Explain what the code does. 2. Identify three limitations. 3. Suggest improvements. 4. Do not rewrite the whole application. 5. Ask me two questions to test my understanding.

The handout's `book_appointment` and `display_appointments` code was pasted after the prompt.

**Part D (alternative version):**

> Create a simple, beginner-friendly Python function that stores a patient name, practitioner name and appointment time. Do not use a database or a GUI.

## What I accepted, changed or rejected

| AI suggestion | Decision | Reason |
| --- | --- | --- |
| Check for double bookings | Accepted (Part G) | Duplicate bookings are a problem the clinic reported, and the test showed the code allowed them. |
| Validate practitioner and time | Accepted, not yet built | Part G allows exactly one improvement. |
| Store the time as a real date and time | Kept unverified | The client has not said which format the clinic uses. |
| Save to a file or database | Rejected for now | The Stage 1 lab says no database. |
| The AI's own version of the function | Not adopted | It accepts a blank patient name and crashes on `None`. |

## How the AI output was checked

- The handout code and the AI version were both run with the same five inputs: a normal appointment, a blank patient name, the same practitioner and time twice, `patient_name=None` and `appointment_time=None`.
- The results are recorded in `comparison.md` and in the completed lab handout.
- The Part G change was tested before and after: the duplicate booking was accepted before the change and rejected after it, and the other four results stayed the same.
