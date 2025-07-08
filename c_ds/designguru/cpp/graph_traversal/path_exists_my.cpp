#include <vector>
#include <iostream>
using namespace std;

class Solution {
    auto dfs(vector<vector<int>>& edges, int start, int end){
    }
public:
    bool validPath(int n, vector<vector<int>>& edges, int start, int end){
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
