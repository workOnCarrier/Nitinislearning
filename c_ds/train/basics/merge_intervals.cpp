#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

template <typename Stream, typename T>
Stream& operator<< (Stream& stream, vector<T> elements){
    stream << "[";
    for ( auto element : elements){
        stream << element << ", ";
    }
    stream << "] ";
    return stream;
}


class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        cout << "\t inputs:" << intervals << endl;
        vector<vector<int>> result;
        std::sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b){return a[0] < b[0];});
        cout << "\t sorted inputs:" << intervals << endl;
        for ( auto interval : intervals){
            if ( result.size() == 0){
                result.push_back(interval);
            } else {
                cout << "\t\t -- " << result[result.size()-1] << " -- interval:" << interval << endl;
                if (result[result.size()-1][1] >= interval[0]){
                    result[result.size()-1][1] = std::max(result[result.size()-1][1], interval[1]);
                } else {
                    result.push_back(interval);
                }
            }
            cout << result << endl;
        }
        return result;
    }
};
void test(){
    // vector<vector<int>> intervals = [[1,3],[2,6],[8,10],[15,18]];
    // vector<vector<int>> intervals = {{2,6},{1,3},{1,4},{8,10},{15,18}};
    vector<vector<int>> intervals = {{1,4},{4,5}};
    Solution s;
    auto final_list = s.merge(intervals);
    cout << "\t for input:" << intervals <<  "\n\t merged:" << final_list << endl;
}


int main(){
    test();
    return 0;
}