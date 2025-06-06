using namespace std;

#include <iostream>
#include <vector>

class Solution {
  void display_swap(vector<int>& arr, int left, int right){
    cout << "swapping -> arr[" << left << "]:" << arr[left] << " -/- arr[" << right << "]:" << arr[right] << endl;
  }
  void swap(vector<int>& arr, int left, int right){
    display_swap(arr, left, right);
    int place_holder = arr[left];
    arr[left] = arr[right];
    arr[right] = place_holder;
  }
  void display_array( vector<int>& arr){
    for ( auto elem: arr){
      cout << elem << ", ";
    }
    cout << endl;
  }
public:
  vector<int> sort(vector<int> &arr) {
    int left = 0;
    int right = arr.size()-1;
    int offset = 0;
    while (offset <= right){
      display_array(arr);
       cout << "left: " << left << ", offset: " << offset  << ", right:" << right << endl;
      if ( arr[offset] == 0){
        if (offset == left){ 
          offset ++;
        } else {
          swap(arr, left, offset);
       }
       left ++;
       continue;
      }
      if (arr[offset] == 2){
        swap(arr, offset, right);
        right --;
        continue;
      }
      offset ++;
    }

    return arr;
  }
};

int main(int argc, char *argv[]) {
  Solution sol;
  vector<int> arr = {1, 0, 2, 1, 0};
  arr = sol.sort(arr);
  for (auto num : arr) {
    cout << num << " ";
  }
  cout << endl;
  cout << "-----------" << endl;

  arr = vector<int>{2, 2, 0, 1, 2, 0};
  arr = sol.sort(arr);
  for (auto num : arr) {
    cout << num << " ";
  }
}
