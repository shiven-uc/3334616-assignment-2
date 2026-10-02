# AI Usage - Week 7 (Stage 4)

- **Tool used:** ChatGPT
- **Note on the tool:** the unit materials name UC-approved tools such as Microsoft Copilot. I used Claude instead and am declaring that here.

## What the AI did

| Item | AI contribution |
| --- | --- |
| Tutorial handout | Drafted the answers to Activities 1 to 4 and the exit question. |
| Lab Part A | Drafted the review of the approved UML. |
| Lab Parts B and C (marked "AI OFF") | Wrote `patient.py`, `practitioner.py` and `validation.py`. |
| Lab Part D | Generated the Appointment class, enum and exception in `source-code/appointment_ai_generated.py`. |
| Lab Parts E and G | Drafted the code review and wrote the refactored `source-code/appointment.py`. |
| Lab Part F | Wrote `source-code/manual_checks.py` and ran it (24 of 24 checks passed). |
| Domain Implementation Workbook | Drafted the UML-to-code trace, invariants, composition and inheritance decisions and the pair-programming record, and generated the updated UML diagram. |
| Reflection | Drafted the reflection. |

## Prompt used (Part D, from the handout)

> Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML.

The Appointment class from the approved UML, business rules BR-02, BR-04 and BR-05, and the Patient and Practitioner classes were sent after the prompt.

## What was accepted, changed or rejected

| AI contribution | Decision | Reason |
| --- | --- | --- |
| `AppointmentStatus` enum and `InvalidStatusTransitionError` | Accepted | Agreed in the prompt. |
| Private attributes, read-only properties, constructor type checks | Accepted | They protect BR-02 and BR-05. |
| `status` parameter in the constructor | Rejected | It allowed an appointment to be created as Cancelled, skipping the transition rules. |
| Transition table with `_change_status` helper | Modified | Replaced by a short check in `cancel()` and `complete()`. |
| `complete()` operation | Accepted with a UML change | The COMPLETED status was unreachable without it. |

## How the AI output was checked

- The generated class was compared with the approved UML and the business rules (Lab Part E).
- The AI-generated version was run, which showed that an appointment could be created as Cancelled.
- `manual_checks.py` was run on the final code: valid objects, invalid input, protected state, cancelling, and illegal repeated transitions. All 24 checks passed.
