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
                pass
            elif  rc in cset:
                l = max(cset[rc] + 1,l)
            cset[rc] = r
            ls = max(ls,r-l+1)
        return ls


        