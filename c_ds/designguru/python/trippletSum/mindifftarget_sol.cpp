using namespace std;

#include <algorithm>
#include <iostream>
#include <limits>
#include <vector>

class Solution {
public:
  int searchTriplet(vector<int>& arr, int targetSum) {
    sort(arr.begin(), arr.end());
    int smallestDifference = numeric_limits<int>::max();
    for (int i = 0; i < arr.size() - 2; i++) {
      int left = i + 1, right = arr.size() - 1;
      while (left < right) {
        // comparing the sum of three numbers to the 'targetSum' can cause overflow
        // so, we will try to find a target difference
        int targetDiff = targetSum - arr[i] - arr[left] - arr[right];
        if (targetDiff == 0) {  //  we've found a triplet with an exact sum
          return targetSum;  // return sum of all the numbers
        }

        if (abs(targetDiff) < abs(smallestDifference) ||
              (abs(targetDiff) == abs(smallestDifference) && 
                            targetDiff > smallestDifference)) {
          smallestDifference = targetDiff;  // save the closest difference
        }

        if (targetDiff > 0) {
          left++;  // we need a triplet with a bigger sum
        } else {
          right--;  // we need a triplet with a smaller sum
        }
      }
    }
    return targetSum - smallestDifference;
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
