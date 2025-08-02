#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> visited(n, 0); // 0: unvisited, 1: visiting, -1: safe
        vector<int> result;

        for (int i = 0; i < n; ++i) {
            if (dfs(graph, visited, i)) {
                result.push_back(i);
            }
        }

        sort(result.begin(), result.end()); // Sorting the result
        return result;
    }

private:
    bool dfs(const vector<vector<int>>& graph, vector<int>& visited, int node) {
        if (visited[node] == -1) return true; // If node is marked as safe
        if (visited[node] == 1) return false; // If node is part of a cycle

        visited[node] = 1; // Mark the node as visiting
        for (int next : graph[node]) {
            if (!dfs(graph, visited, next)) {
                return false; // If any adjacent node is not safe
            }
        }

        visited[node] = -1; // Mark the node as safe
        return true;
    }
};

int main() {
    Solution sol;
    vector<vector<int>> graph1 = {{1,2},{2,3},{2},{},{5},{6},{}};
    vector<vector<int>> graph2 = {{1,2},{2,3},{5},{0},{},{},{4}}; 
    vector<vector<int>> graph3 = {{1,2,3},{2,3},{3},{},{0,1,2}};


    auto res1 = sol.eventualSafeNodes(graph1);
    for (int node : res1) cout << node << " ";
    cout << endl;

    auto res2 = sol.eventualSafeNodes(graph2);
    for (int node : res2) cout << node << " ";
    cout << endl;

    auto res3 = sol.eventualSafeNodes(graph3);
    for (int node : res3) cout << node << " ";
    cout << endl;

    return 0;
}
