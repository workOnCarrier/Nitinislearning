#include <iostream>

using namespace std;
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string result;
        if (word1.length() == 0) return word2;
        if (word2.length() == 0) return word1;
        auto full_len = word1.length() + word2.length();
        result.resize(full_len);
        int offset_1 = 0, offset_2 = 0;
        for (auto offset = 0; offset < full_len; offset ++){
            if ((offset % 2) == 0){
                if (offset/2 < word1.length()){
                    result[offset] = word1[offset_1 ++];
                }else{
                    result[offset] = word2[offset_2 ++];
                }
            }else{
                if (offset / 2 < word2.length()){
                    result[offset] = word2[offset_2 ++];
                }else{
                    result[offset] = word1[offset_1 ++];
                }
            }
        }
        return result;
    }
};


int main(){
    Solution s;
    string word1_1 = "abc";
    string word2_1 = "pqr";
    std::cout << s.mergeAlternately(word1_1, word2_1) << std::endl;

    string word1_2 = "abc";
    string word2_2 = "p";
    std::cout << s.mergeAlternately(word1_2, word2_2) << std::endl;

    string word1_3 = "a";
    string word2_3 = "pqr";
    std::cout << s.mergeAlternately(word1_3, word2_3) << std::endl;
    return 0;
}