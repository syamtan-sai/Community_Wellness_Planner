# Phase 1 Design

## Data structures
- `sessions`: dictionary keyed by session ID; each value stores session details and attendance.
- `participants`: dictionary keyed by participant ID; each value stores the participant name.
- `registrations`: dictionary keyed by session ID; each value is a list of participant IDs.
- `feedback`: dictionary keyed by session ID; each value is a list of feedback dictionaries.

## Workflow
1. Organizer publishes a session.
2. A known participant registers if capacity is available.
3. Organizer marks attendance for registered participants.
4. Registered participants submit a rating and comment.
5. Organizer views a report.

## Attendance percentage
Attendance percentage = (number attended / number registered) × 100.
If no one registered, the percentage is defined as 0 to avoid division by zero.
