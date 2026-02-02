from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tfreq, sfreq = defaultdict(int), defaultdict(int)
        for tc in t:
            tfreq[tc] += 1
            sfreq[tc] = 0
        fl, fr = 0, len(s) - 1 
        l, r = 0, 0
        metc, reqc = 0, len(tfreq)
        found = False
        print(f"\t {tfreq} \n {sfreq}")
        while r < len(s):
             #print(f"\t {metc} {reqc} {s[r]} \t {sfreq}")
            if s[r] in sfreq:
                sfreq[s[r]] += 1
                if sfreq[s[r]] == tfreq[s[r]]:
                    metc += 1
            while metc == reqc:
                found = True
                if s[l] in sfreq:
                    if (fr - fl) > (r - l) :
                        fr = r
                        fl = l
                    sfreq[s[l]] -= 1
                    if sfreq[s[l]] != tfreq[s[l]]:
                        metc -= 1
                l += 1
            r += 1
        print(f"\t found:{found}")
        print(f"\t {fl}: {fr} --- {l}: {r} \t {sfreq}")
        return s[fl:fr + 1] if found else ""

            
def test():
    s="aaaaaaaaaaaabbbbbcdd"
    t="abcdd"
    sol = Solution()
    res = sol.minWindow(s, t)       
    print(f"\t {len(res)}  {res}")

if __name__ == "__main__":
    test()