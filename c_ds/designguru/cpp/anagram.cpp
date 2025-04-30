#include <iostream>
#include <unordered_map>

class Solution {
  std::unordered_map<char, int> char_count;
public:
    bool isAnagram(std::string s, std::string t) {
      size_t current {0};
      auto end {s.size() -1};
      while(current < end){
        char_count[s[current]]++;
        current ++;
      }
      current = 0;
      end = t.size() -1;
      while(current < end){
        char_count[s[current]]--;
        current ++;
      }
      for (const auto& [key, value]: char_count){
        if (value != 0) return false;
      }
      return true;
    }
};

