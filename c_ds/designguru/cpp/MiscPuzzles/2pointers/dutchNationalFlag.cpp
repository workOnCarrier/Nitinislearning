using namespace std;

#include <iostream>
#include <vector>

class Solution {
public:
  vector<int> sort(vector<int> &arr) {
    // TODO: Write your code here
    auto swap = [&arr](int left, int right){
      int tmp = arr[left];
      arr[left] = arr[right];
      arr[right] = tmp;
    };
    int index = 0;
    int low = 0;
    int end = arr.size() -1 ;
    while ( index <= end){
      if ( arr[index] == 0 ){
        swap(low, index);
        ++ low ;
        ++ index ;
      }else if ( arr[index] == 1 ){
        ++ index;
      }else {
        swap(index, end);
        -- end;
      }
    }
    return arr;
  }
};
