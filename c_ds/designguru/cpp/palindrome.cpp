/*
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: sentence = "A man, a plan, a canal, Panama!"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: sentence = "Was it a car or a cat I saw?"
Output: true
Explanation: Explanation: "wasitacaroracatisaw" is a palindrome.

*/
#include <iostream>
#include <cctype>

class Solution {
public:
    bool isPalindrome(std::string s){
        int i = 0, j = s.length() -1;
        if (j < i) return true;
        while ( i < j){
            if(!isalnum(s[i])){ i++; continue;}
            if( !isalnum(s[j])){ j--; continue;}
            if (tolower(s[i]) != tolower(s[j])) { return false; }
            i++; j--;
        }
        return true;
    }
};
void run(const std::string & input, bool expected){
    Solution sol_obj;
	auto output =  sol_obj.isPalindrome(input) ;
	std::cout << output << ":" ;
	if (output == expected){
		std::cout << "expectation matched" << std::endl;
	}else{
		std::cout << "expectation DID NOT matched" << std::endl;
	}
}
void tc1(){
	std::string input {"aeiou"};
	bool expected {false};
	run(input, expected);
}
void tc2(){
	std::string input {""};
	bool expected {true};
	run(input, expected);
}
void tc3() {
    std::string input =  {"A man, a plan, a canal, Panama!"};
    bool expected {true};
    run (input, expected);
}
void tc4() {
    std::string input =  {"race a car"};
    bool expected {false};
    run (input, expected);
}
void tc5() {
    std::string input =  {"Was it a car or a cat I saw?"};
    bool expected {true};
    run (input, expected);
}
void tc6() {
    std::string input =  {""};
    bool expected {true};
    run (input, expected);
}
int main(){
    tc1();
    tc2();
    tc3();
    tc4();
    tc5();
    tc6();
	return 0;
}
