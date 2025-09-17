using namespace std;

#include <algorithm>
#include <iostream>
#include <vector>

class Solution {
public:
  static vector<vector<int>> searchQuadruplets(vector<int> &arr, int target) {
    vector<vector<int>> quadruplets;
    sort(begin(arr), end(arr));
    cout << "[";
    for ( auto val : arr) cout << val << ", " ;
    cout << "]" << " --:" << target << endl;
    if ( arr.size() < 4) return quadruplets;
    int quard = target;
    int offset = 0;
    while( offset < arr.size() - 3 ) {
      int left = offset + 1;
      while ( left < arr.size() - 2 ) {
        int middle = left + 1;
        int right = arr.size() - 1 ;
        while ( middle < right)  {
          quard = arr[offset] + arr[left] + arr[middle] + arr[right];
          cout << offset << ", " << left << ", " << middle << ", " << right << " --:" << quard  << endl;
          if ( quard == target ){
            quadruplets.push_back({ arr[offset] , arr[left] , arr[middle] , arr[right] });
            ++ middle;
            -- right;
            while ( middle < right && arr[middle] == arr[middle - 1]) ++middle;
            while ( middle < right && arr[right] == arr[right + 1]) --right;
            cout << offset << ", " << left << ", " << middle << ", " << right << " --:--" << quard  << endl;
          } else if ( quard > target ){
            -- right;
            while ( middle < right && arr[right] == arr[right + 1]) --right;
          }else {
            ++ middle ;
            while ( middle < right && arr[middle] == arr[middle - 1]) ++middle;
          }
        }
        int same = arr[left];
        while ( same == arr[left]) ++left;
      }
      int same = arr[offset];
      while ( same == arr[offset]) ++offset;
    }
    return quadruplets;
  }
};

template < typename T, typename S>
S& operator << ( S& s, const vector<T> &vals){
    s << "[";
    for ( auto val: vals) s << val << ", ";
    s << "]";
    return s;
}
void test(){
    // vector<int> input{-2, -1, 0, 1, 2, 3};
    vector<int> input{-3, -2, -1, 0, 1, 2, 3};
    vector<vector<int>> expected{{-3,0,2,3},{-2,-1,2,3},{-2,0,1,3},{-1,0,1,2}};
    int target = 2;
    Solution s;
    cout << "\t input:" << input << "__ " << input.size()-1 << endl;
    auto output = s.searchQuadruplets(input,target);
    cout << "\t output:" << output << endl;
    cout << "\t expect:" << expected << endl;
}

int main(){
    test();
    return 0;
}