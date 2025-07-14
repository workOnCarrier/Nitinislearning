
#include <vector>
#include <bits/stdc++.h>
using namespace std;

class Solution {
    void display_input(vector<vector<int>>& isConnected){
        std::cerr << " {\n";
        for (auto row = 0; row < isConnected.size(); ++row){
            std::cerr << "  { ";
            for (auto col = 0; col < isConnected[row].size(); ++col){
                std::cerr << " " << isConnected[row][col] ;
            }
            std::cerr << " }\n";
        }
        std::cerr << " }\n";
    }

public:
    void dfs(vector<vector<int>>& isConnected, vector<bool>& visited, int i) {
        for (int j = 0; j < isConnected.size(); j++) {
            if (isConnected[i][j] == 1 && !visited[j]) {
                visited[j] = true;
                dfs(isConnected, visited, j);
            }
        }
    }

    int findProvinces(vector<vector<int>>& isConnected) {
        int provinces = 0;
        vector<bool> visited(isConnected.size(), false);
        display_input(isConnected);
        for (int i = 0; i < isConnected.size(); i++) {
            if (!visited[i]) {
                dfs(isConnected, visited, i);
                provinces++;
            }
        }
        return provinces;
    }
};

// Main method for testing
int main() {
    Solution solution;

    // Example 1
    vector<vector<int>> example1 = {{1, 1, 0}, {1, 1, 0}, {0, 0, 1}};
    printf("%d\n", solution.findProvinces(example1)); // Expected Output: 2

    // Example 2
    vector<vector<int>> example2 = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
    printf("%d\n", solution.findProvinces(example2)); // Expected Output: 3

    // Example 3
    vector<vector<int>> example3 = {{1, 0, 0, 1}, {0, 1, 1, 0}, {0, 1, 1, 0}, {1, 0, 0, 1}};
    printf("%d\n", solution.findProvinces(example3)); // Expected Output: 2

        // Example 4
    vector<vector<int>> example4 = {{1,1,0,0,0},{1,1,0,0,0},{0,0,1,1,1},{0,0,1,1,0},{0,0,1,0,1}};
    printf("%d\n", solution.findProvinces(example4)); // Expected Output: 2

    return 0;
}
