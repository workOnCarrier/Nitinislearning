#include <unordered_map>
#include <iostream>

using namespace std;

class Solution {
public:
    string decodeMessage(string key, string message) {
        std::unordered_map<char, int> keyMap;
        int key_decode_offset = 0;
        string charmap = "abcdefghijklmnopqrstuvwxyz";
        string result;
        result.resize(message.length());
        for (auto key_char : key){
            if ( key_char == ' ') continue;
            if ( keyMap.find(key_char) == keyMap.end()){
                keyMap[key_char] = int(charmap[key_decode_offset]);
                key_decode_offset ++;
            }
        }
        int decode_offset = 0;
        for (auto enchar: message){
            if (enchar == ' '){
                result[decode_offset]  = enchar;
                decode_offset ++;
            }else{
                result[decode_offset] = char(keyMap[enchar]);
                decode_offset ++;
            }
        }
        return result;
    }
};

void test(){
    Solution s;
    string key = "the quick brown fox jumps over the lazy dog";
    string message = "vkbs bs t suepuv";
    cout << "\t message:" << message << "\n\t decoded:" << s.decodeMessage(key, message) << endl;
}

int main(){
    test();
    return 0;
}