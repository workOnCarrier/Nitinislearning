#include <iostream>
#include <vector>

using namespace std;

template <typename T, typename K>
T& operator<<(T& stream, vector<K>values){
    stream << "[";
    for (auto val: values){
        stream << val << ",";
    }
    stream << "]";
    return stream;
}

class Solution {
public:
    void dfs(vector<int>& nums, vector<int>& currPermute, vector<vector<int>>& result){
        if (nums.size() > 0) {
            for (auto num: nums){
                vector<int> numsLess1;
                for ( auto val : nums){
                    if (val != num) numsLess1.push_back(val);
                }
                currPermute.push_back(num);
                dfs(numsLess1, currPermute, result);
                currPermute.erase(--currPermute.end());
            }
        }else{
            result.push_back(currPermute);
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        
        for (auto num: nums){
            vector<int> currPerm;
            vector<int> numsLess1;
            currPerm.push_back(num);
            for ( auto val : nums){
                if (val != num) numsLess1.push_back(val);
            }
            dfs(numsLess1, currPerm, result);
        }
        return result;
    }
};

void test(){
    vector<int> nums {1,2,3};
    Solution s;
    auto permutations = s.permute(nums);
    cout << "\t result:" << permutations << endl;

}

int main(){
    test();
    return 0;
}