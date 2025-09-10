#include <iostream>
#include <vector>
#include <string>
#include <limits>

using namespace std;

class Solution {
public:
    int shortestWordDistance(vector<string>& wordsDict, string word1, string word2) {
        int last_word1_loc = -1;
        int last_word2_loc = -1;
        auto min_dist = numeric_limits<int>::max();
        for (int index = 0; index < wordsDict.size(); index++){
            auto cur_word = wordsDict[index];
            cout << "\t\t cur_word[" << index << "]:" << cur_word << endl;
            if (cur_word == word1){
                last_word1_loc = index;
                if ( last_word2_loc != -1 && last_word1_loc != last_word2_loc){
                    min_dist = min(min_dist, abs(last_word1_loc - last_word2_loc));
                 }
            }
            if (cur_word == word2){
                last_word2_loc = index;
                if ( last_word1_loc != -1 && last_word1_loc != last_word2_loc) {
                    min_dist = min(min_dist, abs(last_word1_loc - last_word2_loc));
                }
            }
            cout << "\t word1:" << last_word1_loc << " word2:" << last_word2_loc << "\t dist:" << min_dist << endl;
        }
        return min_dist;
    }
};

void test(){
    string word1{"makes"};
    string word2{"coding"};
    vector<string> wordsDict{"practice", "makes", "perfect", "coding", "makes"};
    Solution s;
    auto distance = s.shortestWordDistance(wordsDict, word1, word2);
    cout << distance << endl;
}


int main(){
    test();
    return 0;
}