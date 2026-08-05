class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        ls = 1
        l = 0
        cset = {s[0]:0}
        for r in range(len(s)):
            rc = s[r]
            if r == l:
                print(f"passed when r is {r}")
                pass
            elif  rc in cset:
                l = max(cset[rc] + 1,l)
                print(f"L set to {l}, when r is {r}")
            cset[rc] = r
            print(f" window len is {r-l+1}")
            ls = max(ls,r-l+1)
        return ls


        