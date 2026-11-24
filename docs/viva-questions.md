# Viva-voce preparation

## Why use functions?
Functions divide the program into small tasks, improve readability and allow each operation to be tested separately.

## Why use dictionaries?
Dictionaries associate a unique ID with a record, making it convenient to retrieve a session or participant.

## Why use lists?
A session can have multiple registered participants, attendees and feedback entries. Lists store these collections.

## How is capacity enforced?
The program compares the number of registered participants with the session's capacity before appending a participant ID.

## How is attendance calculated?
Attendance percentage = attended participants / registered participants × 100.

## Is the data permanent?
No. Phase 1 stores records in memory. They are reset when the program exits.
