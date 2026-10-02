# AI Usage - Week 5 (Stage 2)

- **Tool used:** ChatGPT)
- **Note on the tool:** the unit materials name UC-approved tools such as Microsoft Copilot. I used Claude instead and am declaring that here.

## What the AI did

| Item | AI contribution |
| --- | --- |
| Tutorial handout | Drafted the answers to Activities 1 to 4 and the exit question. |
| Lab Parts A to E (marked "AI OFF") | Drafted the notes on the brief, stakeholders, scope, and the first-draft functional requirements, non-functional requirements, user stories and acceptance criteria. |
| Lab Part F | Reviewed the first draft using the reviewer prompt from the handout and returned ten review points, each labelled as evidence-based or as a question or assumption. |
| Lab Part G | Drafted the Accepted / Modified / Rejected / Unverified decision and the evidence for each review point. |
| Lab Part H and the Requirements Specification | Drafted the final SmartCare v0.2 specification, including the business rules, assumptions and open questions. |
| Reflection | Drafted the reflection. |

## Prompt used (Part F, from the handout)

> Act as a software requirements reviewer. Review the SmartCare requirements for ambiguity, inconsistency, missing clarification questions and testability. Do NOT invent new client requirements. For every suggestion, state whether it is based on evidence or is only a question/assumption requiring validation.

The first-draft requirements from Lab Parts B to E were sent after the prompt.

## What was accepted, changed or rejected

| AI suggestion | Decision | Reason |
| --- | --- | --- |
| Define "duplicate booking" | Accepted | The brief reports duplicate bookings, and the draft wording could not be tested. |
| Split "cancel and reschedule" | Modified | Cancelling is in the case study. Rescheduling is not, so it became an open question. |
| Split the patient search | Accepted | One requirement should describe one capability. |
| List the statuses, including No-show | Modified | Booked, Cancelled and Completed kept as an assumption. No-show rejected. |
| Cancelled appointments do not block the time slot | Accepted | Recorded as business rule BR-04. |
| Say whose appointment history is shown | Accepted | Now a patient's appointment history. |
| Make "basic reports" specific | Modified | One provisional report kept, with a question for the client. |
| Make "easy to use" and "fast" measurable | Modified | Targets added and marked as assumptions. |
| Complete the cancel acceptance criterion | Accepted | It now checks the status and that the record is kept. |
| Add a login and user roles | Unverified | Not in the brief. Recorded as an open question only. |

## How the AI output was checked

- Every requirement and every review point was compared with the wording of the client brief and the case study.
- Anything without evidence in the brief was marked as provisional, as an assumption (A-01 to A-04) or as an open question (Q-01 to Q-06) instead of being written as a confirmed requirement.
- Each functional requirement was checked to describe one capability that can be observed and tested.
