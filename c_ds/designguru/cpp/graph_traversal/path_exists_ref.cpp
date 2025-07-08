#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int start, int end) {
        vector<vector<int>> graph(n);
        
        // Create graph from edges
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);  // Undirected graph
        }
        
        vector<bool> visited(n, false);
        return dfs(graph, start, end, visited);
    }

private:
    bool dfs(vector<vector<int>>& graph, int node, int end, vector<bool>& visited) {
        if (node == end) return true;  // Found the path
        visited[node] = true;
        
        // Traverse neighbors
        for (int neighbor : graph[node]) {
            if (!visited[neighbor] && dfs(graph, neighbor, end, visited)) {
                return true;
            }
        }
        return false;  // Path not found
    }
};

int main() {
    Solution sol;
    vector<vector<int>> edges1 = {{0,1},{1,2},{2,3}};
    cout << sol.validPath(4, edges1, 0, 3) << endl;  // true
    vector<vector<int>> edges2 = {{0,1},{2,3}};
    cout << sol.validPath(4, edges2, 0, 3) << endl;  // false
    vector<vector<int>> edges3 = {{0,1},{3,4}};
    cout << sol.validPath(5, edges3, 0, 4) << endl;  // false
}
