#include <iostream>
#include <vector>

using namespace std;

template <typename Stream, typename T>
Stream& operator<< (Stream &stream, const vector<T>& inputs){
    stream << "[" ;
    for (auto val : inputs){
        stream << val << ", ";
    }
    stream << "]";
    return stream;
}

class Solution {
public:
    vector<int> goodIndices(vector<int>& nums, int k) {
        vector<int> dp1(nums.size(), 1);
        vector<int> dp2(nums.size(), 1);
        vector<int> result;
        cout << "\t\t inp:" << nums << endl;
        // non increasing
        for (int index = 1; index < nums.size(); ++index){
            if (nums[index] <= nums[index-1]) dp1[index] += dp1[index-1];
            cout <<  "\t\t index:" << index << " dp1[index]:" << dp1[index] << " dp1[index-1]:" << dp1[index-1] << endl;
        }
        cout << "\t\t dp1:" << dp1 << endl;
        // non decreasing
        for (int rindex = nums.size()-1; rindex > 0; --rindex){
            if (nums[rindex - 1] <= nums[rindex]) dp2[rindex-1] += dp2[rindex];
        }
        cout << "\t\t dp2:" << dp2 << endl;
        for (int res = k; res < nums.size()-k; ++res){
            if (dp1[res-1] >= k && dp2[res+1] >= k) result.push_back(res);
        }
        return result;
    }
};

void test(){
    vector<int> input {2,1,1,1,3,4,1};
    Solution s;
    auto result = s.goodIndices(input, 2);
    cout << "\t result:" << result << endl;
}

int main(){
    test();
    return 0;
}