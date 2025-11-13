class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        req_len = len(s1)
        if len(s2) < req_len:
            return False
        req_code, sub_code = [0]* 26,  [0]* 26
        for index in range(len(s1)):
            req_code[ord(s1[index]) - ord('a')] += 1
            sub_code[ord(s2[index]) - ord('a')] += 1
        match_count = 0
        for i in range(26):
            match_count += 1 if req_code[i] == sub_code[i] else 0
        
        start = 0
        for in_ in range(len(s1), len(s2)):
            if match_count == 26:
                return True
            ic = ord(s2[in_]) - ord('a')
            sub_code[ic] += 1
            if sub_code[ic] == req_code[ic]:
                match_count += 1
            elif sub_code[ic] - 1 == req_code[ic]:
                match_count -= 1
            og = ord(s2[start]) - ord('a')
            sub_code[og] -= 1
            if sub_code[og] == req_code[og]:
                match_count += 1
            elif sub_code[og] + 1 == req_code[og]:
                match_count -= 1
            start += 1
        return match_count == 26