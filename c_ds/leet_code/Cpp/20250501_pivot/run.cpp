#include <iostream>
#include <vector>

using namespace std;

class Solution {
    long getsum(vector<int>& nums){
        long sum = 0;
        for (auto element: nums){
            sum += element;
        }
        return sum;
    }
public:
    int findMiddleIndex(vector<int>& nums) {
        // find sum of the full array
        long sum = getsum(nums);
        // check first index is pivot
        // if (nums.size() > 1 && sum-nums[0] == 0 )
        //     return 0;
        // check last index is pivot
        // if (nums.size() > 1 && sum-nums[nums.size()-1] == 0)
        //     return nums.size()-1 ;
        // now we need to find the actual index
        long left_sum = 0;
        int potential_pivot = 0;
        for(; potential_pivot < nums.size(); potential_pivot++){
            long remaining_sum = sum - nums[potential_pivot];
            cout << "left_sum:" << left_sum << " remaining_sum:" << remaining_sum << endl;
            if (left_sum  == remaining_sum) return potential_pivot;
            left_sum += nums[potential_pivot];
            sum = remaining_sum;
        }
        return -1;
        
    }
};

void test(){
    vector<int> input = {3, 2, -1 -4, 8};
    auto sol = Solution();
    auto pivot = sol.findMiddleIndex(input);
    if (pivot == 1) cout << "successful" << endl;
    else cout << "failed: " << pivot << " is not equal to " << 1 << endl;
}


int main(){
    test();

    return 0;
}