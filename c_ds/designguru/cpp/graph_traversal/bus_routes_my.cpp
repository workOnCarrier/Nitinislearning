/*
You are given an array routes where routes[i] is the list of bus stops that the bus travels in a cyclic manner. For example, if routes[0] = [2, 3, 7], it means that bus 0 travels through the stops 2 -> 3 -> 7 -> 2 -> 3 -> 7 ... and then repeats this sequence indefinitely.

You start at a bus stop called source and wish to travel to a bus stop called target using the bus routes. You can switch buses at any bus stop that is common to the routes of two buses.

Return the minimum number of buses you need to take to travel from source to target. If it is not possible to reach the target, return -1.
*/

#include <iostream>
#include <vector>
#include <deque>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;
    void display(vector<vector<int>> routes){
        std::cout << "\t[";
        for (auto route = 0; route < routes.size(); route++){
            std::cout <<  "route:" << route << " stops:[";
            for (auto stop : routes[route]){
                std::cout << stop << ", ";
            }
            std::cout << "], ";
        }
        std::cout << "]" << std::endl;;
    }

class Solution {
    void display(unordered_map<int, unordered_set<int>> &bussesAtStop){
        std::cout <<  "\t";
        for (auto [stop, busses]: bussesAtStop){
            std::cout << stop << ":[";
            for (auto busNo : busses){
                std::cout << busNo << ", ";
            }
            std::cout << "], ";
        }
        std::cout << endl;
    }
    bool dfs(vector<vector<int>>& routes, unordered_map<int, unordered_set<int>>& bussesAtStop, int currStop, int target, deque<int> &busRiding){
        if (busRiding.empty()){
            std::cout << "BusRiding is empty" << endl;
            return false;
        }
        auto currBus = busRiding.back();
        std::cout << "\t riding:" << currBus << "\t at stop:" << currStop << "\t with trip len:" << busRiding.size() << " (";
        for (auto val: busRiding) std::cout << val << ", " ;
        cout << ")" << endl;
        auto currBusRouteStops = routes[currBus];
        for ( auto stop : currBusRouteStops){
            if (currStop == stop) continue;
            if (stop == target) return true;
            auto busesAtNewStop = bussesAtStop[stop];
            for ( auto nextBus: busesAtNewStop ){
                cout << "\t at stop:" << stop  << " attempting bus:" << nextBus << endl;
                if (busRiding.end() != find(busRiding.begin(), busRiding.end(), nextBus)) continue;
                busRiding.push_back(nextBus);
                auto isTargetOnRoute = dfs(routes, bussesAtStop, stop, target, busRiding);
                if (isTargetOnRoute) return true;
                busRiding.pop_back();
            }
        }
        std::cout << endl;
        return false;
    }
public:
    // Method to find the minimum number of buses required to travel from source to target
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        deque<int>  busRiding;
        unordered_map<int, unordered_set<int>> bussesAtStop;
        for ( auto route = 0 ; route < routes.size(); route++){
            vector<int> stops = routes[route];
            for (auto stop : stops){
                if (bussesAtStop.find(stop) == bussesAtStop.end()){
                    bussesAtStop[stop] = unordered_set<int>();
                }
                bussesAtStop[stop].insert(route);
            }
        }
        display(bussesAtStop);
        auto startBus = *(bussesAtStop[source].begin());
        busRiding.push_back(startBus);
        std::cout << "\t startBus:" << startBus << std::endl;
        auto targetOnRoute = dfs(routes, bussesAtStop, source, target, busRiding);
        return targetOnRoute? busRiding.size() : -1;
    }
};

int main() {
    Solution solution;

    // Example 1
    vector<vector<int>> routesA = {{2, 3, 4}, {5, 6, 7, 8}, {4, 5, 9, 10}, {10, 12}};
    display( routesA );
    cout << solution.numBusesToDestination(routesA, 3, 12) << endl; // Output: 3

    // Example 2
    vector<vector<int>> routesB = {{1, 2, 3, 4, 5}, {5, 6, 7, 8}, {8, 9, 10, 11}};
    cout << solution.numBusesToDestination(routesB, 1, 11) << endl; // Output: 3

    // Example 3
    vector<vector<int>> routesC = {{1, 2, 5}, {3, 6, 7}, {7, 9, 10}};
    cout << solution.numBusesToDestination(routesC, 2, 10) << endl; // Output: -1

    return 0;
}

