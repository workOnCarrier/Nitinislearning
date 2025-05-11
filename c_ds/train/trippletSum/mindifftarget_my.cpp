using namespace std;

#include <algorithm>
#include <iostream>
#include <limits>
#include <vector>

class Solution {
public:
  int searchTriplet(vector<int>& arr, int targetSum) {
    // TODO: Write your code here
    std::sort(arr.begin(), arr.end());
    for (auto elem : arr) cout << elem << ", " ;
    cout << endl;
    int near_sum = std::numeric_limits<int>::max();
    for ( int base_offset = 0; base_offset < arr.size()-2; base_offset ++ ){
      int left = base_offset + 1;
      int right = arr.size() -1;
      while (left < right){
        int pos_sum = arr[base_offset] + arr[left] + arr[right];
        int targetDiff = targetSum - pos_sum;
        if (targetDiff == 0) {
          return targetSum; // return sum of all the numbers
        }
        cout << " ->" << arr[base_offset] << ", " <<  arr[left] << ", " <<  arr[right] << " :: " << targetDiff << " : " << near_sum  << " : " << targetSum << endl;

        if ( abs(targetDiff)  < abs(near_sum)  )  {
          near_sum = targetDiff;
          cout << "  ---- nearsum: " << near_sum << endl;
        }
        if ( targetDiff > 0 ) {
          left ++; cout << "  ---- add left for: " << targetDiff << endl;
        } else {
          right --; cout << "  ---- reduce right for: " << targetDiff << endl;
        }
      }
    }
    return targetSum - near_sum;
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
