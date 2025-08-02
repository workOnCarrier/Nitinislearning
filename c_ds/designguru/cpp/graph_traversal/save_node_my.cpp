/*
You are given a directed graph with n nodes, labeled from 0 to n-1. This graph is described by a 2D integer array graph, where graph[i] is an array of nodes adjacent to node i, indicating there is a directed edge from node i to each of the nodes in graph[i].

A node is called a terminal node if it has no outgoing edges. A node is considered safe if every path starting from that node leads to a terminal node (or another safe node).

Return an array of all safe nodes in ascending order.
*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
private:
    void displayNode(int index, vector<vector<int>>& graph){
        cout << "Node:" << index ;
        cout << " children:" ;
        for (auto childNode: graph[index]) cout << childNode << ", ";
        cout << endl;
    }
    bool dfs(int index, vector<vector<int>>& graph, vector<int> &visited){
        // displayNode(index, graph);
        if (visited[index] == 1) return false; // -- unsafe
        if (visited[index] == -1) return true; // -- safe
        visited[index] = 1;
        auto childNodes = graph[index];
        for ( auto childIndex : childNodes){
            auto isChildSafe = dfs(childIndex, graph, visited);
            if (!isChildSafe) return false;
        }
        visited[index] = -1;
        return true;
    }
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        auto nodeCount = graph.size();
        vector<int>   result;
        vector<int>   visited(nodeCount, 0);
        for (auto node = 0; node < nodeCount; node++){
            auto isSafe = dfs(node, graph, visited);
            if (isSafe) result.push_back(node);
        }
        sort(result.begin(), result.end());
        return result;
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
