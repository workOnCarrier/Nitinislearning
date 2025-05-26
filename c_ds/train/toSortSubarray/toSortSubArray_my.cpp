using namespace std;

#include <iostream>
#include <limits>
#include <vector>

class Solution {
public:
  static int sort(const vector<int>& arr) {
    for (auto elem: arr) cout << elem << ", " ;
    cout << endl;
    int left = -1;
    int right = -1;
    for ( int current = 0; current < arr.size()-1; current++ ){
      if (arr[current] > arr[current+1]){
        left = current;
        cout << " checking left:" << left << " for " << arr[current] << "|" << arr[current+1] << endl;
        break;
      }
    }
    for ( int rc = arr.size()-1; rc > left; rc -- ){
      if (arr[rc] < arr[rc-1]){
        right = rc;
        cout << " checking right:" << right << " for " << arr[rc] << "|" << arr[rc-1] << endl;
        break;
      }
    }

    int subarrayMax = numeric_limits<int>::min(), subarrayMin = numeric_limits<int>::max();
    for (int k = left; k <= right; k++) {
      subarrayMax = max(subarrayMax, arr[k]);
      subarrayMin = min(subarrayMin, arr[k]);
    }

    while (left > 0 && arr[left - 1] > subarrayMin) {
      left--;
    }
    while (right < arr.size() - 1 && arr[right + 1] < subarrayMax) {
      right++;
    }
    cout << " final ::" << left << ":" << right << " for " << arr[left] << "|" << arr[right] << endl;
    if (right != left) return right - left + 1;
    else if ( right !=-1 or left != -1) return 1;
    return 0;
  }
};


int main(int argc, char* argv[]) {
  Solution sol;
  cout << sol.sort(vector<int>{1, 2, 5, 3, 7, 10, 9, 12}) << endl;
  cout << sol.sort(vector<int>{1, 3, 2, 0, -1, 7, 10}) << endl;
  cout << sol.sort(vector<int>{1, 2, 3}) << endl;
  cout << sol.sort(vector<int>{3, 2, 1}) << endl;
  cout << sol.sort(vector<int>{1, 3, 2, 4}) << endl;
}
