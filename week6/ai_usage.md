# AI Usage - Week 6 (Stage 3)

- **Tool used:** ChatGPT
- **Note on the tool:** the unit materials name UC-approved tools such as Microsoft Copilot. I used Claude instead and am declaring that here.

## What the AI did

| Item | AI contribution |
| --- | --- |
| Tutorial handout | Drafted the candidate concepts table, CRC cards, relationship reasoning and the critique of the AI proposals. |
| Lab Parts A to D (the "AI OFF" steps) | Drafted the noun, verb and business rule review, the candidate classes, the first-draft CRC cards and the first-draft UML diagram. |
| Lab Part E | Suggested classes and relationships from the confirmed requirements, with requirement IDs (suggestions S1 to S8). |
| Lab Part F | Drafted the accepted, modified and rejected decisions. |
| Lab Part G | Wrote the class skeletons in `source-code/smartcare_v03.py`. |
| Lab Part H | Wrote `source-code/check_model.py` and ran it (27 of 27 checks passed). |
| Domain Model Workbook | Drafted the requirement-to-concept trace, CRC cards, design rationale and AI review record, and generated both UML diagrams. |
| Reflection | Drafted the reflection. |

## Prompt used (Part E)

> Suggest classes and relationships for the SmartCare system using only the confirmed requirements below. For every class and relationship, give the IDs of the requirements that support it. Do not use provisional requirements, assumptions or open questions.

The SmartCare v0.2 functional requirements and business rules were sent after the prompt.

## What was accepted, changed or rejected

| AI suggestion | Decision | Reason |
| --- | --- | --- |
| Patient, Practitioner and Appointment as classes | Accepted | Already in the first draft. |
| Status as an enumeration | Accepted | FR-09 and BR-05. A fixed list prevents inconsistent status values. |
| An ID for each appointment | Accepted | BR-04 means two appointments can share a practitioner and time. |
| `is_booked` on Appointment | Accepted | Keeps the BR-01 and BR-04 rule in one place. |
| Appointment lists inside Patient and Practitioner | Modified | Multiplicities kept. The lists were not added, to avoid storing the same fact twice. |
| Person superclass | Rejected | No requirement supports it. |
| Schedule class with time slots | Rejected | Working hours are an open question (Q-04). |
| Receptionist class | Rejected | Staff are users of the system. Logins are an open question (Q-05). |

## How the AI output was checked

- Every class, attribute, operation and relationship was traced to a requirement or business rule in SmartCare v0.2 (see the trace table in the workbook).
- Suggestions with no confirmed requirement behind them were rejected.
- `check_model.py` compares the code with the final UML diagram. All 27 checks passed.
