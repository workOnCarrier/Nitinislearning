using namespace std;

#include <iostream>
#include <vector>

class Solution
{
public:
    int countIslands(vector<vector<int>> &matrix)
    {
        int rows = matrix.size();
        int cols = matrix[0].size();
        int totalIslands = 0;
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                if (matrix[i][j] == 1) // only if the cell is a land
                {
                    // we have found an island
                    totalIslands++;
                    visitIslandDFS(matrix, i, j);
                }
            }
        }
        return totalIslands;
    }

private:
    static void visitIslandDFS(vector<vector<int>> &matrix, int x, int y)
    {
        if (x < 0 || x >= matrix.size() || y < 0 || y >= matrix[0].size())
            return; // return, if it is not a valid cell
        if (matrix[x][y] == 0)
            return; // return, if it is a water cell

        matrix[x][y] = 0; // mark the cell visited by making it a water cell

        // recursively visit all neighboring cells (horizontally & vertically)
        visitIslandDFS(matrix, x + 1, y); // lower cell
        visitIslandDFS(matrix, x - 1, y); // upper cell
        visitIslandDFS(matrix, x, y + 1); // right cell
        visitIslandDFS(matrix, x, y - 1); // left cell
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
