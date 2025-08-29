#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool rotateString(string s, string goal) {
        if (s.length() != goal.length()) return false;
        int slen = s.length();

        for ( int rot_count = 0; rot_count < slen; rot_count++ ) {
            rotate ( s.begin(), s.begin()+1, s.end() );
            if ( s == goal ) return true;
        }
        return false;
    }
};

void test(){
    Solution s;

    {
    string input = "abcdefg";
    string goal = "defgabc";
    cout << input << " -|- " << goal << "\t match status:" << s.rotateString(input, goal) << endl;
    }
    string input = "abcdefg";
    string goal = "d";
    cout << input << " -|- " << goal << "\t match status:" << s.rotateString(input, goal) << endl;
}

int main(){
    test();
    return 0;
}