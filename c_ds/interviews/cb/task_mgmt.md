Task Management System (in-memory)

Design and implement an in-memory task management system that supports tasks, users, task assignment with TTL (time-to-live), and time-based completion/expiration rules.
Entities
Task : id (unique), name , priority (higher number = higher priority, or clearly define).
User : id (unique), and a quota = maximum number of active task assignments the user may have at once.
Task Assignment : assigns a task to a user at a startTime , with a ttl (duration). The assignment is active on [startTime, startTime + ttl) and expired at or after startTime + ttl .
Requirements / APIs
Task CRUD
Create a task.
Get a task by id.
Update a task (e.g., name/priority).
Task listing
Return the top N tasks by priority.
Return the top N tasks by priority whose name contains a given substring .
Users + assignment with TTL
Add a user with a quota.
Assign a task to a user with a TTL at a given startTime .
You may assign multiple tasks to the same user .
You may assign the same task to multiple users .
(If the same task is assigned multiple times to the same user at different start times, treat them as distinct assignments.)
List a user’s active tasks at a given time t .
Completion + expiration rules
Complete a task for a user at a given time t .
You cannot complete an expired assignment.
If there are multiple active assignments for the same (userId, taskId) , completing that taskId completes the one with the earliest startTime .
List a user’s expired tasks at a given time t .
Clarifications to state during the interview
How ties in priority are broken (e.g., higher priority first, then by taskId lexicographically).
Whether “list tasks by priority” returns tasks (unique by taskId) or assignments (can repeat taskId). (Common approach: listing in (2) is over tasks; user lists in (3)/(4) are over assignments.)
Input constraints and expected complexity (aim for efficient queries; in-memory only).