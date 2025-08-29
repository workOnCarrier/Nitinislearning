class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        if len(word1) == 0:
            return word2
        if len(word2) == 0:
            return word1
        full_len = len(word1) + len(word2)
        offset_1, offset_2 = 0, 0
        for offset in range(full_len):
            is_1 = (offset % 2) == 0
            if is_1:
                if offset // 2 <  len(word1):
                    result += word1[offset_1]
                    offset_1 += 1
                else:
                    result += word2[offset_2]
                    offset_2 += 1
            else:
                if offset // 2 <  len(word2):
                    result += word2[offset_2]
                    offset_2 += 1
                else:
                    result += word1[offset_1]
                    offset_1 += 1
        return result
 
        
def main():
    s = Solution()
    word1_1 = "abc"
    word2_1 = "pqr"
    print(s.mergeAlternately(word1_1, word2_1))

    word1_2 = "abc"
    word2_2 = "p"
    print(s.mergeAlternately(word1_2, word2_2))

    word1_3 = "a"
    word2_3 = "pqr"
    print(s.mergeAlternately(word1_3, word2_3))

if __name__ == "__main__":
    main()
