#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int climbStairs(int n) {
        if (n == 1) return 1;
        vector<int> steps(n+1, 0);
        steps[1] = 1;
        steps[2] = 2;
        for (auto level = 3; level < n+1; level++){
            steps[level] = steps[level - 1] + steps[level - 2];
        }
        return steps[n];
    }
};


int main(){
    Solution s;
    cout << s.climbStairs(1) << endl;
    cout << s.climbStairs(2) << endl;
    cout << s.climbStairs(4) << endl;
}