/*
Given an undirected graph, represented as a list of edges. Each edge is illustrated as a pair of integers [u, v], signifying that there's a mutual connection between node u and node v.
You are also given starting node start, and a destination node end, return true if a path exists between the starting node and the destination node. Otherwise, return false.
*/
#include <vector>
#include <map>
#include <iostream>
#include <stdexcept>
#include <sstream>
#include <format>
using namespace std;

class Solution {
    template<typename T>
    string getEdgeVectorStr(std::vector<T> edges){
        stringstream ss;
        for (auto val : edges) {
            ss << " " << val ;
        }
        return ss.str();
    }
    bool dfs(map<int, vector<int>>& edges, int current, int end, vector<bool> visited){
        std::cerr << std::format("\tcurrent:{} end:{}", current, end) << endl;
        if ( current == end) return true;
        visited[current] = true;
        if (edges.find(current) == edges.end()) return false;
        auto edgesForCurr = edges[current];
        std::cerr << std::format("\t\t current:{} edges:{}", current, getEdgeVectorStr(edgesForCurr)) << endl;
        for ( auto dest : edgesForCurr){
            if (!visited[dest] && dfs(edges, dest, end, visited)) return true;
        }
        return false;
    }
public:
    bool validPath(int n, vector<vector<int>>& edges, int start, int end){
        vector<bool> visited;
        for ( int cur_val = 0; cur_val < n; cur_val++) visited.push_back(false);
        map<int, vector<int>> pathsMap;
        for ( auto edge : edges){
            if (pathsMap.end() == pathsMap.find(edge[0]) ) pathsMap[edge[0]] = vector<int>(); 
            if (pathsMap.end() == pathsMap.find(edge[1]) ) pathsMap[edge[1]] = vector<int>(); 
            pathsMap[edge[0]].push_back(edge[1]);
            pathsMap[edge[1]].push_back(edge[0]);
        }
        std::cerr << std::format("\t visited before traversal:{}", getEdgeVectorStr(visited)) << endl;
        return dfs(pathsMap, start, end, visited);
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
