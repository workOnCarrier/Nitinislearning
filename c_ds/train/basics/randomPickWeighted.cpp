#include <vector>
#include <cstdlib>
#include <ctime>
#include <iostream>

using namespace std;

template <typename Stream, typename T>
Stream& operator<< (Stream& stream, const vector<T>& values){
    stream << "\t\t vector:[";
    for (auto val: values){
        stream << val << ", ";
    }
    stream << "]" << endl;
    return stream;
}

class Solution {
    vector<int> m_prefixSum;
public:
    Solution(vector<int>& w):m_prefixSum(w.size()) {
        for (int offset = 0; offset < w.size(); ++offset){
            m_prefixSum[offset] = ( offset == 0 ? 0 : m_prefixSum[offset -1] ) + w[offset] ;
        }
        srand(RAND_MAX);
        cout << "\t\t prefixSum:" << m_prefixSum << endl;
    }
    int pickIndex() {
        float randNum = (float) rand() / RAND_MAX;
        float target = randNum * m_prefixSum.back();
        cout << "\t\t randNum:" << randNum << " target:" << target << endl;
        // return  lower_bound(begin(m_prefixSum), end(m_prefixSum), target) - begin(m_prefixSum);
        // return index;
        int left = 0, right = m_prefixSum.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (m_prefixSum[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
};

void run(vector<int> input, int query_count = 1){
    cout << input << endl;
    Solution s(input);
    cout << "\t result:";
    for (int val = 0; val < query_count; ++val ){
        auto result = s.pickIndex();
        cout << "\t index value:" << result << endl;
    }
    cout << endl;
}

void test(){
    vector<int> input{1};
    run(input);
    input.push_back(3);
    run(input, 5);
    input[1] = 7;
    input.push_back(8);
    run(input, 5);
}
void custom_test(){
    vector<int> input{3, 14, 1, 7};
    run(input, 5);
}

int main(){
    test();
    custom_test();
    return 0;
}