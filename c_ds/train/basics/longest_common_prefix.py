class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        cur_pos = 0
        result = ""
        valid = False
        while cur_pos < len(strs):
            cur_char = strs[0][cur_pos]
            valid = True
            for val in strs:
                if cur_char == val[cur_pos]:
                    continue
                else:
                    valid = False
                    break
            if valid == False:
                break
            result += cur_char
            cur_pos += 1
        return result


def test():
    strs = ["flower","flow","flight"]
    s = Solution()
    longest_str = s.longestCommonPrefix(strs)
    print(f"\t result:{longest_str}")

if __name__ == "__main__":
    test()