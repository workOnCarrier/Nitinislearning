#include <iostream>
#include <vector>

using namespace std;

class Solution{
public:
    int countIslands(vector<vector<int>> &input){
        int islandCount = 0;
        int matrix_size = input.size();
        for (auto row = 0; row < matrix_size; row++){
            for (auto col = 0; col < matrix_size; col++){
                islandCount += this->dfs(row, col, matrix_size - 1, input);
            }
        }
        return islandCount;
    }

    int dfs(int row, int col, int matrix_size, vector<vector<int>>& input){
        if (row < 0 || row > matrix_size || col < 0 || col > matrix_size) return 0;
        if (input[row][col] == 0) return 0;
        input[row][col] = 0;
        dfs(row-1, col, matrix_size, input);
        dfs(row+1, col, matrix_size, input);
        dfs(row, col-1, matrix_size, input);
        dfs(row, col+1, matrix_size, input);
        return 1;
    }

};


int main(int argc, char **argv)
{
    Solution sol;

    vector<vector<int>> vec = vector<vector<int>>{
        {1, 1, 1, 0, 0},
        {0, 1, 0, 0, 1},
        {0, 0, 1, 1, 0},
        {0, 0, 1, 0, 0},
        {0, 0, 1, 0, 0}};
    cout << sol.countIslands(vec) << endl;

     vec = {
        {0, 1, 1, 1, 0},
        {0, 0, 0, 1, 1},
        {0, 1, 1, 1, 0},
        {0, 1, 1, 0, 0},
        {0, 0, 0, 0, 0}};
    cout << sol.countIslands(vec) << endl;

    return 0;
};
