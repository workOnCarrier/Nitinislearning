using namespace std;

#include <algorithm>
#include <iostream>
#include <vector>

class Solution {
public:
  int searchTriplets(vector<int> &arr, int target) {
    int count = 0;
    sort(arr.begin(), arr.end());
    if (arr.size() < 3) return 0;
    for ( int offset = 0; offset < arr.size() - 2 ; offset++){
      int left = offset +1;
      int right = arr.size()-1;
      while ( left < right){
        int sum = arr[offset] + arr[left] + arr[right] ;
        if (sum < target){
          count += right - left;
          left++;
        }else{
          right --;
        }
      }
    }
    for ( auto elem : arr) cout << elem << ", ";
    cout << " --: target :" << target << "   ==:" << count << endl;
    return count;
  }
};
