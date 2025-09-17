using namespace std;

#include <algorithm>
#include <iostream>
#include <vector>

class Solution {
public:
  static vector<vector<int>> searchQuadruplets(vector<int> &arr, int target) {
    vector<vector<int>> quadruplets;
    if (arr.size() < 4) return quadruplets;
    sort(arr.begin(), arr.end());
    int offset = 0;
    while (offset < arr.size() - 3){
      int left = offset +1;
      int right = arr.size() - 1;
      while (left < right - 1){
        int middle = left +1;
        while ( middle < right) {
          long sum = arr[offset] + arr[left] + arr[middle] + arr[right];
          if (sum <= target){
            if (sum == target) quadruplets.push_back({arr[offset] , arr[left] , arr[middle] , arr[right]});
            int same = arr[middle];
            while(same == arr[middle]) middle++;
          } else {
            int same = arr[right];
            while (same == arr[right]) right--;
          }
        }
        int same = arr[left];
        while( same == arr[left]) left ++;
        right = arr.size() -1;
      }
      int same = arr[offset];
      while (same == arr[offset])offset++;
    }
    return quadruplets;
  }
};
