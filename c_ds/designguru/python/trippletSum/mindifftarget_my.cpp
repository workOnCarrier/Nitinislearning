using namespace std;

#include <algorithm>
#include <iostream>
#include <limits>
#include <vector>

class Solution {
public:
  int searchTriplet(vector<int>& arr, int targetSum) {
    // TODO: Write your code here
    if (arr.size() < 3) throw runtime_error("invalid input: insufficient size of array");
    sort(arr.begin(), arr.end());
    int near_sum = numeric_limits<int>::max();
    for(int offset = 0; offset < arr.size() -2; offset++){
      int curr_sum = 0;
      int left = offset + 1;
      int right = arr.size() -1;
      while ( left < right){
        curr_sum = arr[offset] + arr[left] + arr[right];
        cout <<  arr[offset] << ", " << arr[left] << ", " <<  arr[right] ;
        cout << " :: " << curr_sum << " : " << near_sum << endl;
        if ( targetSum == curr_sum ){
          return targetSum;
        }
        if ( abs(targetSum - curr_sum) < abs(targetSum - near_sum) ||
              (curr_sum < near_sum && abs(targetSum - curr_sum) == abs(targetSum - near_sum))){
          near_sum = curr_sum;
          cout << "near_sum:" << near_sum << endl;
        }
        if ( targetSum > curr_sum){
          left++;
        }else{
          right--;
        }
      }
    } 
    return near_sum;
  }
};


int main(int argc, char* argv[]) {
  Solution sol;
  vector<int> vec = {-1, 0, 2, 3};
  cout << sol.searchTriplet(vec, 2) << endl;
  vec = {-3, -1, 1, 2};
  cout << sol.searchTriplet(vec, 1) << endl;
  vec = {1, 0, 1, 1};
  cout << sol.searchTriplet(vec, 100) << endl;
  vec = {0, 0, 1, 1, 2, 6};
  cout << sol.searchTriplet(vec, 5) << endl;
}
