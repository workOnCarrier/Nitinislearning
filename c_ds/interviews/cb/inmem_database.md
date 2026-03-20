# software Engineer
You are asked to implement a small in-memory “database” that evolves across 4 parts. In each part you may reuse your previous code and only add/extend methods.
Data model
Each record is identified by a string key and stores a string value. Time is represented by an integer timestamp t (monotonically increasing in tests).
Part 1 — Basic read/write

Implement a database supporting:
put(key, value, t) : store value for key .
get(key, t) -> value | null : return the currently stored value for key , or null if missing.
Notes:
If put is called multiple times for the same key, the latest write should be returned.
Part 2 — Scan

Add:
scan(prefix, t) -> List<(key, value)> : return all key/value pairs whose key starts with prefix .
Requirements:
Results must be sorted by key in lexicographic order.
Part 3 — Expiration (TTL)

Extend put to optionally accept a TTL:
put(key, value, t, ttlSeconds) means the entry is valid for timestamps in the half-open interval [t, t + ttlSeconds) . After that it is expired.
Update get and scan so that expired items are not returned.
Clarifications:
If a key is overwritten with a new put , the new value/TTL replaces the old one.
Keys without TTL never expire.
Part 4 — Backup / Restore

Add support for backups:
backup(t) -> backupId : captures the database state at time t (only non-expired entries at time t ).
restore(backupId, t) : restores the database to exactly the state captured in that backup.
TTL behavior on restore:
If an entry had remaining TTL at backup time, it should still expire after the remaining time elapses following the restore (i.e., expiration is based on the original timestamps/remaining lifetime, not “reset” to a fresh TTL).
What you need to deliver
Implement the required methods so that all provided test cases pass.
Constraints (typical for this style of OA)
Up to ~10^5 operations.
Keys/values are short strings.
Aim for efficient lookups and scans.
