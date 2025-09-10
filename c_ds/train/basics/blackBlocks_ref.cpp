
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

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
        int res[5] = {0};
        unordered_map<long long , int> map;
        for(int i = 0, len = coordinates.size(); i < len; ++i){
            int xs = coordinates[i][0];
            int ys = coordinates[i][1];
            int xend = min(xs + 1 , m - 1);
            int yend = min(ys + 1 , n - 1);
            for(int x = max(0 , xs - 1); x < xend; ++x){
                for(int y = max(0 , ys - 1); y < yend; ++y){
                    ++map[((1LL * x) << 17) | y];
                }
            }
        }
        for(auto& [_ , cnt] : map) ++res[cnt];
        long long Blocks = 1LL * (m - 1) * (n - 1);
        return {Blocks - (int)map.size(), res[1], res[2], res[3], res[4]};
    }
};

void test(){
    vector<vector<int>> coordinates{{0,0},};
    Solution s;
    auto result = s.countBlackBlocks(3, 3, coordinates);
    cout << result << endl;
}
void test_2(){
    vector<vector<int>> coordinates {{37,54},{40,64},{25,84},{29,11},{38,49},{9,16},{38,41},{19,76},{15,7},{13,41},{16,62},{39,25},{13,77},{5,75},{24,66},{19,24},{36,57},{29,39},{37,21},{39,49},{23,51},{23,16},{21,76},{8,9},{12,46},{27,25},{11,8},{37,70},{20,57},{31,0},{34,62},{30,20},{7,27},{14,80},{43,16},{25,46},{36,72},{25,36},{22,55},{15,33},{38,56},{28,8},{18,42},{40,20},{13,1},{13,0},{31,51},{3,64},{11,81},{1,49},{40,53},{3,28},{38,24},{37,31},{30,26},{22,5},{35,79},{10,81},{42,4},{1,10},{11,25},{27,11},{21,43},{37,49},{20,8},{5,68},{39,21},{36,4},{28,64},{35,71}} ;
    Solution s;
    auto result = s.countBlackBlocks(45, 85, coordinates);
    cout << result << endl;
}


int main(){
    test_2();
    return 0;
}