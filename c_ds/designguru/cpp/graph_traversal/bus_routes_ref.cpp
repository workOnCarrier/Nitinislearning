#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Solution {
public:
    // Method to find the minimum number of buses required to travel from source to target
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        if (source == target)
            return 0; // If source and target are the same, no bus is needed

        // Map bus stops to buses that visit them
        unordered_map<int, vector<int>> stopToBuses;
        for (int i = 0; i < routes.size(); ++i) {
            for (int stop : routes[i]) {
                stopToBuses[stop].push_back(i);
            }
        }

        // BFS setup
        queue<pair<int, int>> q;
        unordered_set<int> visitedStops;
        unordered_set<int> usedBuses;

        q.push({source, 0}); // Start BFS with the source stop and 0 buses taken
        visitedStops.insert(source); // Mark the source stop as visited

        while (!q.empty()) {
            auto current = q.front();
            q.pop();
            int stop = current.first;
            int buses = current.second;

            for (int bus : stopToBuses[stop]) {
                if (usedBuses.count(bus))
                    continue; // Skip buses that have already been used
                usedBuses.insert(bus); // Mark the current bus as used

                for (int nextStop : routes[bus]) {
                    if (nextStop == target)
                        return buses + 1; // Found the target stop
                    if (!visitedStops.count(nextStop)) {
                        visitedStops.insert(nextStop);
                        q.push({nextStop, buses + 1}); // Enqueue the next stop with one more bus taken
                    }
                }
            }
        }

        return -1; // If target is not reachable, return -1
    }
};

// Main method to test the solution with provided examples
int main() {
    Solution solution;

    // Example 1
    vector<vector<int>> routesA = {{2, 3, 4}, {5, 6, 7, 8}, {4, 5, 9, 10}, {10, 12}};
    cout << solution.numBusesToDestination(routesA, 3, 12) << endl; // Output: 3

    // Example 2
    vector<vector<int>> routesB = {{1, 2, 3, 4, 5}, {5, 6, 7, 8}, {8, 9, 10, 11}};
    cout << solution.numBusesToDestination(routesB, 1, 11) << endl; // Output: 3

    // Example 3
    vector<vector<int>> routesC = {{1, 2, 5}, {3, 6, 7}, {7, 9, 10}};
    cout << solution.numBusesToDestination(routesC, 2, 10) << endl; // Output: -1

    return 0;
}
