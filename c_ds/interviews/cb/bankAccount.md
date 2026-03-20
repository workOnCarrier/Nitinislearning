Problem A — Banking system command processor

Implement an in-memory banking system that processes a sequence of commands in timestamp order.
Entities
Account identified by a unique string accountId .
Balance is a non-negative integer amount.
Commands (examples shown; you may define an equivalent input format)
CREATE accountId
Create a new account with balance 0.
If the account already exists, the command should be handled deterministically (e.g., ignore or error).
DEPOSIT accountId amount
Add amount to the account.
TRANSFER fromId toId amount
Move funds from fromId to toId if sufficient funds exist.
TOP_SPENDERS k
Return the top k accounts ranked by total outgoing spend (e.g., sum of successful TRANSFER amounts sent by the account). Define deterministic tie-breaking (e.g., by accountId ).
SCHEDULE_PAYMENT fromId toId amount executeAt
Schedule a delayed transfer to run at time executeAt .
Scheduled payments should execute automatically at/after their scheduled time when processing later commands.
CANCEL_PAYMENT paymentId
Cancel a previously scheduled payment if it has not executed.
MERGE targetId sourceId
Merge sourceId into targetId :
targetId receives sourceId ’s remaining balance.
Define what happens to scheduled payments involving sourceId (e.g., re-point to targetId , or cancel), and ensure the behavior is consistent.
BALANCE accountId
Output the current balance.
Output
Return outputs for query-like commands (e.g., TOP_SPENDERS, BALANCE, possibly errors) in the order encountered.
Notes / constraints
Assume up to large numbers of commands; aim for efficient data structures.
Clearly define edge-case behavior (invalid accounts, negative amounts, cancel-after-execute, merge semantics, etc.).