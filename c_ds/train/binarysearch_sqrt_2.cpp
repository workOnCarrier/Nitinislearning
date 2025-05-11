#include <iostream>
using namespace std;

class Solution {
public:
  int mySqrt(int x) {
    std::cout << "input:" << x << std::endl;
    int mid = 0;
    int left = 2;
    if (x < left) return x;
    int right = x/2;
    while (left <= right){
      cout << "left:" << left << endl;
      cout << "right:" << right << endl;
      mid = left + (right - left)/2;
      long result = (long)mid * mid;
      std::cout << "result:" << result << std::endl;
      if (result > x) {right = mid-1; }
      if (result < x) {left = mid+1; }
      if (result == x) {
        cout << " -- breaking:" << mid << endl;
        return mid;
      }
    }
    cout << "----- final value:" << right  << endl;
    return right;
  }
};
int main() {
  Solution solution;

  int input1 = 4;
  int expectedOutput1 = 2;
  int result1 = solution.mySqrt(input1);
  std::cout << (result1 == expectedOutput1) << std::endl; // Expected output: 1

  int input2 = 8;
  int expectedOutput2 = 2;
  int result2 = solution.mySqrt(input2);
  std::cout << (result2 == expectedOutput2) << std::endl; // Expected output: 1

  int input4 = 2;
  int expectedOutput4 = 1;
  int result4 = solution.mySqrt(input4);
  std::cout << (result4 == expectedOutput4) << std::endl; // Expected output: 1

  int input5 = 3;
  int expectedOutput5 = 1;
  int result5 = solution.mySqrt(input5);
  std::cout << (result5 == expectedOutput5) << std::endl; // Expected output: 1

  int input6 = 15;
  int expectedOutput6 = 3;
  int result6 = solution.mySqrt(input6);
  std::cout << (result6 == expectedOutput6) << std::endl; // Expected output: 1

  int input7 = 2147395600;
  int expectedOutput7 = 46340;
  int result7 = solution.mySqrt(input7);
  std::cout << (result7 == expectedOutput7) << std::endl; // Expected output: 1

  return 0;
}
