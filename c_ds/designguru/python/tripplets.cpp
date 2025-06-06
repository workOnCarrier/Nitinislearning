using namespace std;

#include <algorithm>
#include <iostream>
#include <vector>

class Solution {
public:
  static vector<vector<int>> searchTriplets(vector<int> &arr) {
    vector<vector<int>> triplets;
    int full_len_offset = arr.size() -1;
    sort(arr.begin(), arr.end());
    // for ( auto val: arr){cout << val << ", " ;} cout << endl;
    for (int base_ptr = 0; base_ptr<= full_len_offset - 2; base_ptr++){
      int left = base_ptr + 1;
      int right = full_len_offset;
      if (base_ptr > 0 && arr[base_ptr] == arr[base_ptr - 1]) {
        continue; // skip same element to avoid duplicate triplets
      }
      cout << " base:" << arr[base_ptr] << endl;;
      while (left < right){
        cout << " try left:" << arr[left] << endl;
        cout << " try right:" << arr[right] << endl;
        if ((arr[left] + arr[right] + arr[base_ptr]) < 0) left++; 
        else if ((arr[left] + arr[right] + arr[base_ptr]) > 0) right--;
        else {
          cout << "base:" << arr[base_ptr] << " left:" << arr[left] << " right:" << arr[right] << endl;;
          triplets.push_back({arr[base_ptr], arr[left], arr[right]});
          left++; right --;
          while (left < right && arr[left] == arr[left - 1]) {
            left++; // skip same element to avoid duplicate triplets
          }
          while (left < right && arr[right] == arr[right + 1]) {
            right--; // skip same element to avoid duplicate triplets
          }
        }
      }
    }
    return triplets;
  }
};
int main(int argc, char *argv[]) {
  Solution sol;
  auto check = [&](vector<int> &vec){
  auto result = sol.searchTriplets(vec);
  for (auto vec : result) {
    cout << "[";
    for (auto num : vec) {
      cout << num << " ";
    }
    cout << "]";
  }
  cout << endl;
  };

  vector<int> vec = {-3, 0, 1, 2, -1, 1, -2};
  check(vec);
  vec = {-5, 2, -1, -2, 3};
  check(vec);
  
  vec = {0, 0, 0};
  check(vec);  

  vec = {-1,0,1,2,-1,-4};
  check(vec);
}
