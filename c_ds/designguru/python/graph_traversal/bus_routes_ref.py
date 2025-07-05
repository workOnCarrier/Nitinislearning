from collections import defaultdict, deque
from typing import List

class Solution:
    # Method to find the minimum number of buses required to travel from source to target
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0  # If source and target are the same, no bus is needed

        # Map bus stops to buses that visit them
        stop_to_buses = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(i)

        # BFS setup
        queue = deque()
        visited_stops = set()
        used_buses = set()

        queue.append((source, 0))  # Start BFS with the source stop and 0 buses taken
        visited_stops.add(source)  # Mark the source stop as visited

        while queue:
            current = queue.popleft()  # Dequeue the current stop and buses taken
            stop, buses = current[0], current[1]

            for bus in stop_to_buses[stop]:
                if bus in used_buses:
                    continue  # Skip buses that have already been used
                used_buses.add(bus)  # Mark the current bus as used

                for next_stop in routes[bus]:
                    if next_stop == target:
                        return buses + 1  # Found the target stop
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses + 1))  # Enqueue the next stop with one more bus taken

        return -1  # If target is not reachable, return -1

# Main method to test the solution with provided examples
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    routesA = [[2, 3, 4], [5, 6, 7, 8], [4, 5, 9, 10], [10, 12]]
    print(solution.numBusesToDestination(routesA, 3, 12))  # Output: 3

    # Example 2
    routesB = [[1, 2, 3, 4, 5], [5, 6, 7, 8], [8, 9, 10, 11]]
    print(solution.numBusesToDestination(routesB, 1, 11))  # Output: 3

    # Example 3
    routesC = [[1, 2, 5], [3, 6, 7], [7, 9, 10]]
    print(solution.numBusesToDestination(routesC, 2, 10))  # Output: -1


