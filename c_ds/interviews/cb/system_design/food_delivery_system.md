Design a food delivery platform (similar to common restaurant delivery apps).
Core user stories

Customers can browse restaurants/menus, place an order, pay, and track delivery.
Restaurants receive orders, confirm/prepare them, and update status.
Delivery partners (couriers) receive assignments, navigate to pickup/dropoff, and update status.
Functional requirements

Restaurant discovery (basic search/filter by location/cuisine).
Menu retrieval.
Order placement and payment.
Order lifecycle: CREATED -> CONFIRMED -> PREPARING -> READY_FOR_PICKUP -> PICKED_UP -> DELIVERED (include cancellation/refund paths).
Real-time-ish tracking/status updates for customers.
Non-functional requirements

High availability for placing orders.
Idempotency for order creation/payment.
Low latency for dispatch.
Support peak traffic (e.g., lunch/dinner spikes).
Follow-ups (mentioned by interviewer)

How would you design the dispatch/matching between orders and couriers?
How would you model and deliver real-time order status updates?
How would you scale search and read-heavy restaurant/menu traffic?
Optimization follow-up: Couriers have limited capacity/time; choose a subset of candidate orders to batch/assign to maximize value under constraints (this can resemble a knapsack -style optimization). Explain your approach at a high level.