#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

struct tuple_hash{
    size_t operator()(const tuple<int, int>& t) const{
        return hash<int>()(get<0>(t)) ^ (hash<int>()(get<1>(t)) << 1);
    }
};
class NumArray {
    vector<int> m_num;
    unordered_map<tuple<int, int>, int, tuple_hash> m_memo;
public:
    NumArray(vector<int>& nums):m_num(nums) { }
    
    void update(int index, int val) {
        m_num[index] = val;
        m_memo.clear();
    }
    
    int sumRange(int left, int right) {
        auto iter = m_memo.find(tuple(left, right));
        if (iter != m_memo.end()){
            return iter->second;
        }
        int sum = 0;
        for(auto index = left; index <= right; index ++){
            sum += m_num[index];
        }
        m_memo.emplace(std::make_pair(tuple(left, right), sum));
        return sum;
    }
};

void test(){
/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */
    vector<int> nums{1, 3, 5};
    NumArray* obj = new NumArray(nums);
    int index = 1;
    int val= 2;
    int left = 0;
    int right = 2;
    int param_2 = obj->sumRange(left,right);
    cout << param_2 << endl;

    obj->update(index,val);
    param_2 = obj->sumRange(left,right);
    cout << param_2 << endl;

}

int main(){
    test();
    return 0;
}