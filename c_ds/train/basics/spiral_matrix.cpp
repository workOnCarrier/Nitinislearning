    
#include <iostream>
#include <tuple>
#include <vector>
#include <functional>
#include <thread>

using namespace std;

auto go_right = [](int row, int col)  { return tuple{row, col + 1 };};
auto go_down = [](int row, int col)   { return tuple{row + 1, col };};
auto go_left = [](int row, int col)   { return tuple{row, col - 1 };};
auto go_up = [](int row, int col)     { return tuple{row - 1, col };};

using Op = std::function< std::tuple<int, int> (int, int) >;

using namespace std::chrono_literals;

template <typename Stream>
Stream& operator << (Stream& stream, const tuple<int, int> val){
    stream << std::get<0>(val) << ", " << std::get<1>(val) << endl;
    return stream;
}

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<char> direction {'r', 'd', 'l', 'u'};
        vector<Op> operations  {go_right, go_down, go_left, go_up};
        vector<Op> oper_uns  {go_left, go_up, go_right, go_down};
        int oper_offset = 0;
        vector<int> result;
        vector<tuple<int,int>> matrix_walk;
        int row_max = matrix.size();
        int col_max = matrix[0].size();
        vector<vector<bool>> visited(row_max, vector<bool>(col_max, false));
        int row = 0;
        int col = 0;
        while (matrix_walk.size() < matrix.size() * matrix[0].size()){
            if ( visited[row][col] || row < 0 || col < 0 || row >= matrix.size() || col >= matrix[0].size() ){
                cout << "\t\t before changing row:" << row << "\t col:" << col << "--- for direction:" << direction[oper_offset] << endl;
                cout << *(std::find(matrix_walk.begin(), matrix_walk.end(), tuple(row, col))) << endl;
                std::tie(row, col) = oper_uns[oper_offset](row, col);
                oper_offset = (oper_offset + 1) % operations.size();
                std::tie(row, col) = operations[oper_offset](row, col);
                cout << "\t\t row:" << row << "\t col:" << col << "--- for direction:" << direction[oper_offset] << endl;
            }else{
                cout << " \t\t adding row:" << row << "\t col:" << col  << endl;
                result.push_back(matrix[row][col]);
                visited[row][col] = true;
                std::tie(row, col) = operations[oper_offset](row, col);
            }
            this_thread::sleep_for(1000ms);
        }
        return result;
    }
};

template <typename Stream, typename T>
Stream& operator<< (Stream& stream, const vector<T>& row){
    stream << "[";
    for (auto data: row){
        stream << data << ", ";
    }
    stream << "]";
    return stream;
}


template <typename Stream, typename T>
Stream& operator<< (Stream& stream, const vector<vector<T>>& matrix){
    stream << "[";
    for (auto row: matrix){
        stream << row <<  ", ";
    }
    stream << "]";
    return stream;
}

void test(){
    vector<vector<int>> matrix {{1,2,3}, {4,5,6}, {7,8,9}};
    Solution s;
    std::vector<int> result = s.spiralOrder(matrix);
    cout << "\tfor matrix:" << matrix << "\n\t spiral result:" << result  << endl;
}

int main(){
    test();
    return 0;
}

        