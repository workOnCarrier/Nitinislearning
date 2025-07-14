/* 
There are n cities. Some of them are connected in a network. If City A is directly connected to City B, and City B is directly connected to City C, city A is indirectly connected to City C.

If a group of cities are connected directly or indirectly, they form a province.

Given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise, determine the total number of provinces.
*/

#include <vector>
#include <iostream>
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
    void dfs_update(vector<vector<int>>& isConnected, int row, int col){
        if (row < 0 ) { return; }
        if ( row >= isConnected.size() ){ return; }
        if ( col < 0 ){ return; }
        if ( col >= isConnected[row].size() ){ return; }
       if (isConnected[row][col] == 1){
            // std::cerr << " row:" << row << " col:" << col << " ";
            // std::cerr << "(" << row - 1 << ", " << col << "), ";
            // std::cerr << "(" << row + 1 << ", " << col << "), ";
            // std::cerr << "(" << row  << ", " << col - 1 << "), ";
            // std::cerr << "(" << row  << ", " << col + 1 << "), " << endl;
             isConnected[row][col] = 0;
            dfs_update(isConnected, row - 1, col);
            dfs_update(isConnected, row + 1, col);
            dfs_update(isConnected, row , col + 1 );
            dfs_update(isConnected, row , col - 1 );
            // dfs_update(isConnected, row - 1, col - 1 );
            // dfs_update(isConnected, row + 1, col + 1 );
        }
        return;
    }
public:
    // Function to find the province count.
    int findProvinces(vector<vector<int>>& isConnected) {
        int islands = 0;
        display_input(isConnected);
        for (auto row = 0; row < isConnected.size(); ++row){
            for ( auto col = 0;  col < isConnected[row].size(); ++col){
                if ( isConnected[row][col] == 1){
                    ++islands;
                    dfs_update(isConnected, row, col);
                }
            }
        }
        return islands;
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
