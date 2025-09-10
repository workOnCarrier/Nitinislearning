// https://leetcode.com/problems/number-of-black-blocks/?envType=problem-list-v2&envId=vepb0dld

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

template <typename Stream, typename T>
Stream& operator<<(Stream& stream, vector<T> values){
    stream << "[";
    for( auto value: values){
        stream << value << ", ";
    }
    stream << "]";
    return stream;
} 

class Solution {
public:
    vector<long long> countBlackBlocks(int m, int n, vector<vector<int>>& coordinates) {
        vector<long long> result(5, 0);
        for ( auto x = 0; x < m-1; ++ x){
            for ( auto y = 0; y < n-1; ++ y){
                vector<vector<int>> blocks{{x,y}, {x, y+1}, {x+1, y}, {x+1, y+1}};
                cout << "\t block:" << blocks << endl;
                int blacks = 0;
                for ( auto block : blocks){
                    if ( find_if(begin(coordinates), end(coordinates),
                             [&block](vector<int>& coordinate){
                                for (auto index = 0; index < block.size(); ++index){
                                    if (block[index] != coordinate[index]) return false;
                                }
                                return true;
                             }
                        ) != coordinates.end()){
                        ++blacks;
                    }
                }
                result[blacks]++;
            }
        }
        return result;
    }
};


void test(){
    vector<vector<int>> coordinates{{0,0},};
    Solution s;
    auto result = s.countBlackBlocks(3, 3, coordinates);
    cout << result << endl;
}


int main(){
    test();
    return 0;
}