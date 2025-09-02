#include <vector>
#include <iostream>
#include <sstream>

using namespace std;

class Solution{
public:
    string countAndSay(int n){
        string curr_str = "1";
        if ( n <= 1) return curr_str;
        for (int iter = 1; iter < n; iter++){
            stringstream new_str ;
            int curr_ptr = 0;
            int next_change = 0;
            while ( next_change < curr_str.length()) {
                while( curr_str[curr_ptr] == curr_str[next_change]){
                    next_change ++;
                }
                new_str << next_change - curr_ptr <<  curr_str[curr_ptr];
                curr_ptr = next_change;
            }
            curr_str = new_str.str();
        }
        return curr_str;
    }
};

void test(){
    Solution s;
    vector<int> inputs{1, 2, 3,4,5,6,7,8,9} ;
    for (auto input :  inputs){
        cout << "cas for " << input << ": " << s.countAndSay(input) << endl;
    }
}


int main () {
    test();
    return 0;
}