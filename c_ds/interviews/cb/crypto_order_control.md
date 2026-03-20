# software engineer
You are implementing part of a simple crypto trading system that manages client orders. Each order can be in one of several states: NEW, ACTIVE, PAUSED, CANCELLED, or FILLED.
You need to support the following operations for a single order (you can assume order creation is already done):
pause(orderId) : Temporarily pause an active order so that it will not be matched or executed while paused.
resume(orderId) : Resume a paused order so that it becomes active again and can be matched.
cancel(orderId) : Cancel an order so that it will never be executed in the future.
Rules and constraints:
Valid state transitions are:
NEW -> ACTIVE
ACTIVE -> PAUSED
PAUSED -> ACTIVE (on resume)
ACTIVE -> CANCELLED
PAUSED -> CANCELLED
ACTIVE -> FILLED
Once an order is in CANCELLED or FILLED , no further operations ( pause , resume , or cancel ) should change its state.
pause on a non- ACTIVE order should be rejected.
resume on a non- PAUSED order should be rejected.
cancel on a CANCELLED or FILLED order should be a no-op or return an error (choose one behavior and be consistent).
Implement a small in-memory component that:
Stores the current state of each order by orderId .
Exposes methods pause , resume , and cancel that update state according to the rules above.
Returns success/failure for each operation based on whether the transition is allowed.
Describe your data structures and implement the core logic for these operations.