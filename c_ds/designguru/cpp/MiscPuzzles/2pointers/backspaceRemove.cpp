#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
  static bool compare(const string &str1, const string &str2) {
    // TODO: Write your code here
    if ( str1.length() == 0 || str2.length() == 0) return false;
    auto reducedString = [](const string &strInput){
      string str;
      int curr = 0;
      while ( curr < strInput.length()){
        cout << strInput[curr];
        if ( strInput[curr] == '#'){
          cout << "-found #:" << curr << "-";
          str = str.substr(0, str.length()-1);
        }
        else {
          str += strInput[curr];
        }
        ++curr;
      }
      cout << "-" << str << "-" << endl;
      return str;
    };
    string redStr1 = reducedString(str1);
    cout << "\t 1:" << redStr1 << "|" <<  endl;
    string redStr2 = reducedString(str2);
    cout << "\t 2:" << redStr2 << "|" << endl;
    return  (redStr1.find(redStr2) == redStr2.find(redStr1));
  }
};

void test(){
    string str1 = "xyz#";
    string str2 = "xyz##";
    Solution s;
    auto result = s.compare(str1, str2);
    cout << result << endl;
}

int main(){
    test();
    return 0;
}