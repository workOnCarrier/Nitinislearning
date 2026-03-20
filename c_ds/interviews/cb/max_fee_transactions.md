# software engineer
Problem: Max-fee block assembly

You are given N transactions. Each transaction has:
id (unique)
size (positive integer)
fee (non-negative integer)
A block has a maximum capacity B (total size). You must choose a subset of transactions to include in the block such that:
The sum of size of chosen transactions is <= B
The sum of fee is maximized
Input
N transactions: [(id, size, fee), ...]
Block capacity B
Output
The maximum achievable total fee, and/or the list of chosen transaction IDs.
Constraints (example)
1 <= N <= 2000
1 <= B <= 100
1 <= size <= B
0 <= fee <= 10^9

Follow-up: Parent/child dependencies

Now each transaction may optionally have a parent_id. If a transaction is included, all its ancestors must also be included. Assume dependencies form a forest (no cycles).
Choose a valid subset within capacity B that maximizes total fee.
Clarify what you would return if multiple optimal subsets exist (any is fine).