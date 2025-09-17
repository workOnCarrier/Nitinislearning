using namespace std;

#include <algorithm>
#include <iostream>
#include <vector>

template <typename S, typename T>
S& operator << ( S& s, const vector<T>& vals){
  s << "[";
  for ( auto val: vals){
    s << val << ", ";
  }
  s << "]";
  return s;
}

class Solution {
public:
  int searchTriplets(vector<int> &arr, int target) {
    int count = 0;
    // TODO: Write your code here
    sort(begin(arr), end(arr));
    cout << arr << " -- target:" << target << endl;
    for ( auto start = 0; start < arr.size() - 2; ++start ){
      int middle = start + 1;
      int end = arr.size() - 1;
        while ( middle < end) {
        auto triplet = arr[start] + arr[middle] + arr[end];
        cout << "\t start:" << start << " middle:" <<  middle << " end:" <<  end << " triplet:" << triplet <<  endl;
        if ( triplet < target ){
        count += end - middle;
        ++middle;
        }else{
        --end;
        }
    }
    middle = start + 1;
    }
    return count;
  }
};
