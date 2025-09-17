// https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/?envType=problem-list-v2&envId=vepb0dld

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int longestCommonPrefix(vector<int>& arr1, vector<int>& arr2) {
        int max_len = 0;
        auto getPrefix = [](int val){
            vector<int> prefixPack;
            while (val > 0){
                prefixPack.push_back(val);
                val /= 10;
            }
            return prefixPack;
        };
        vector<vector<int>> Pp1(arr1.size());
        vector<vector<int>> Pp2(arr2.size());
        for ( int index = 0; index < arr1.size(); ++index) {
            Pp1[index] = getPrefix(arr1[index]);
        }
        for ( int index = 0; index < arr2.size(); ++index) {
            Pp2[index] = getPrefix(arr2[index]);
        }
        auto getPrefixLen = [](vector<int> p1, vector<int> p2){
            int len = 0;
            int i = p1.size() -1;
            int j = p2.size() -1;
            while( i >= 0 && j >= 0){
                if (p1[i] == p2[j]) {
                    ++len; --i; --j;
                }else break;
            }
            return len;
        };
        for ( int i = 0; i < Pp1.size(); ++i)
            for ( int j = 0; j < Pp2.size(); ++j){
                max_len = max(max_len, getPrefixLen(Pp1[i], Pp2[j]));
            }
        return max_len;
    }
};

void test(){
    vector<int> arr1{1, 10, 100};
    vector<int> arr2{1000};
    Solution s;
    cout << "\t longest prefix len:" << s.longestCommonPrefix(arr1, arr2) << endl;
}


int main(){
    test();
    return 0;
}