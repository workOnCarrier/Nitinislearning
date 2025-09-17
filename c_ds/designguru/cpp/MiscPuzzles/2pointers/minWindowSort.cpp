using namespace std;

#include <iostream>
#include <limits>
#include <vector>

class Solution {
public:
  static int sort(const vector<int>& arr) {
    // TODO: Write your code here
    int left = 0;
    int right = arr.size() -1;
    bool mooveLeft = true;
    bool mooveRight = true;
    while (left < right){
      if ( mooveLeft && arr[left] < arr[left + 1]){
        ++left;
      } else {
        mooveLeft = false;
      }
      if ( mooveRight && arr[right-1] < arr[right]) {
        --right;
      }else {
        mooveRight = false;
      }
      if (arr[right] < arr[left]) {
        mooveRight = false;
        mooveLeft = false;
        while( left > 0 && arr[right] < arr[left - 1 ] ) --left;
      }
      if ( !mooveRight && !mooveLeft) break;
    }
    return right == left? 0 : right - left + 1;
  }
};


void test(){
    vector<int> input{1, 3, 2, 4};
    Solution s;
    auto output  = s.sort(input);
    cout << "\t output:" << output << endl;
}

int main(){
    test();
    return 0;
}