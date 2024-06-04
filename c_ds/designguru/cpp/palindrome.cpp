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
        while ( i < j){
            while ( i < j && !isalnum(s[i])){ i++;}
            while ( i < j && !isalnum(s[j])){ j--;}
            if (tolower(s[i]) != tolower(s[j])) { return false; }
            i++; j--;
        }
        return true;
    }
};
void run(const std::string & input, bool expected){
    Solution sol_obj;
	auto output =  sol_obj.isPalindrome(input) ;
	std::cout << output << std::endl;
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

int main(){
    tc1();
	return 0;
}
