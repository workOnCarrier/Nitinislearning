#include <iostream>
#include <string>

using namespace std;

class Solution {
  template<typename T>
  void swap(std::string &s, T &left_offset, T &right_offset){
    char temp = s[right_offset];
            s[right_offset] = s[left_offset];
            s[left_offset] = temp;
            left_offset++;
            right_offset--;
  }
  public:
  Solution (){}
    std::string reverseVowels(std::string s) {
      // TODO: Write your code here
      std::string vowels = "aeiouAEIOU";
      auto len = s.length();
      if (len == 0) return s;
      std::string::size_type left_offset = 0;
      std::string::size_type right_offset = len-1;
      cout << "left_offset:" << left_offset << "::right offset:" << right_offset << endl;
      while(left_offset < right_offset){
        if ( s.npos == vowels.find(s[left_offset])){
          left_offset ++;
        }
        else{ // keep looking for vowel to swap and only then increment 
          if (s.npos != vowels.find(s[right_offset])){
            swap(s, left_offset, right_offset);
          }else{
            right_offset--;
          }
        }
      }
      return s;
    }
};

void run(const std::string & input, const std::string & expected){
    Solution sol_obj;
	std::string output =  sol_obj.reverseVowels(input) ;
	std::cout << output << std::endl;
	if (output == expected){
		std::cout << "expectation matched" << std::endl;
	}else{
		std::cout << "expectation DID NOT matched" << std::endl;
	}
}
void tc1(){
	std::string input {"aeiou"};
	std::string expected {"uoiea"};
	run(input, expected);
}
void tc2(){
	std::string input {"xyz"};
	std::string expected {"xyz"};
	run(input, expected);
}

void tc3(){
	std::string input {""};
	std::string expected {""};
	run(input, expected);
}


int main(){
    tc3();
	return 0;
}
