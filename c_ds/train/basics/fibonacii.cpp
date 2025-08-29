#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    long long fib(int n) {
        if (n <= 0) return 0;
        long long prev = 1;
        long long prevm1 = 0;
        long long curr = 1;
        for (int pos = 2; pos <= n; pos++){
            curr = prev + prevm1;
            prevm1 = prev;
            prev = curr;
        }
        return curr;
    }
};


int main(){
    Solution s;
    cout << s.fib(5) << endl;
    cout << s.fib(-1) << endl;
    cout << s.fib(1) << endl;
    cout << s.fib(1000) << endl;
    return 0;
}