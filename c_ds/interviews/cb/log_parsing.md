Task 1: Parse and group a log file by thread ID

You are given a list of log lines (strings). Each line contains at least:
a timestamp (parseable and comparable; assume ISO-8601 or an integer epoch),
a thread ID (integer or string),
an arbitrary message .
Example format (you may assume a consistent format across all lines):
2026-02-13T10:15:30Z thread=42 msg=Starting work
Requirements
Parse each line to extract (timestamp, threadId, message) .
Group logs by threadId .
For each threadId , sort that thread’s log entries by timestamp ascending .
Return a structure like Map<threadId, List<LogEntry>> (or Map<threadId, List<String>> preserving original lines) where each list is time-sorted.
Edge cases to handle
Multiple logs with the same timestamp.
Malformed lines (state and apply a reasonable policy: skip, throw, or collect errors).