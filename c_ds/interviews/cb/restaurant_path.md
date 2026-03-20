# software engineer
You are given two independent coding tasks.

Task 1: Shortest paths in a restaurant grid

Context: A restaurant is represented as a 2D grid. The waiter starts from a fixed starting cell and must walk around tables (obstacles) to pick up food items.
Input:
Integers m and n for the grid dimensions.
An m × n grid of characters, where:
S – starting position of the waiter (exactly one cell).
. – empty cell where the waiter can walk.
\# – obstacle (e.g., a table) the waiter cannot pass through.
F – a cell containing a food item.
The waiter can move in 4 directions (up, down, left, right). Each move to an adjacent non-obstacle cell costs 1 step.
Answer the following subproblems:
Single-item shortest path
You are given the coordinates (targetRow, targetCol) of a single food item (an F cell).
Compute the length of the shortest path from S to that cell.
If it is unreachable, return -1 .
All-items shortest path
Now consider all cells marked F as items to be picked up. Starting from S , the waiter must visit every F cell at least once, in any order, and may end anywhere.
Compute the minimum total number of steps required to collect all items, or -1 if it is impossible.
You may assume there are at most k ≤ 12 food items in the grid.
For this task:
Clearly describe the algorithm you would use for each subproblem.
State the time and space complexity in terms of m , n , and the number of items k .
You may be asked to implement functions such as:
int shortestPathToOneItem(char[][] grid, int targetRow, int targetCol)
int shortestPathToAllItems(char[][] grid)



Task 2: Order event processing with idempotency

Context: You are processing a stream of order events consumed from a message queue similar to Kafka. Due to at-least-once delivery, events may be delivered more than once; your processing must be idempotent (re-processing the same logical event should not change the final result more than once).
Each event has the following fields:
eventId (string): unique identifier for a logical event. If the same logical event is delivered multiple times, all its copies share the same eventId .
orderId (string): the order this event belongs to.
type (enum): one of NEW , FILL , CANCEL .
quantity (integer, positive).
timestamp (long, monotonically increasing for simplicity across this stream).
Event semantics:
NEW – creates a new order with total quantity = quantity .
Initial state: OPEN , with filledQuantity = 0 .
FILL – fills quantity units of an existing OPEN or PARTIALLY_FILLED order.
filledQuantity increases.
If filledQuantity == totalQuantity , the order state becomes FILLED .
You may assume you do not receive valid FILL events for an order that is already fully filled or cancelled, except for duplicated events.
CANCEL – cancels an existing order.
If the order is OPEN or PARTIALLY_FILLED , its state becomes CANCELLED .
After an order is cancelled, subsequent non-duplicate fills must not change its state or filled quantity.
Assumptions:
All events for a given orderId arrive in non-decreasing timestamp order.
The global stream may contain duplicate events due to retries, but duplicates always share the same eventId as the original.
You are asked to:
Core processing logic
Design and implement a function that, given a list of events in arrival order, outputs the final state of each order. For each orderId , output:
state in { OPEN , PARTIALLY_FILLED , FILLED , CANCELLED }.
totalQuantity (from the corresponding NEW event).
filledQuantity (sum of effective fills applied to the order).
Idempotency
Ensure your implementation is idempotent with respect to eventId :
If the input list contains duplicate events with the same eventId , only the first occurrence should affect the result; the rest must be ignored.
If you reprocess the same list of events (or a superset that only adds duplicates), the final results for all orders must remain the same.
Design discussion
Describe:
The data structures you use to track orders and to detect duplicate events.
How your logic updates order state for each event type.
How you guarantee idempotency in the presence of duplicate events.
The time and space complexity in terms of the number of events E and the number of distinct orders O .
You may be asked to implement an interface such as:
class Event {
    String eventId;
    String orderId;
    String type;      // values: NEW, FILL, CANCEL
    int quantity;
    long timestamp;
}

class OrderState {
    String state;     // values: OPEN, PARTIALLY_FILLED, FILLED, CANCELLED
    int totalQuantity;
    int filledQuantity;
}

Map<String, OrderState> processEvents(List<Event> events)