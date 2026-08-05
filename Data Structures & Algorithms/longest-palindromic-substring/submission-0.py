class Solution:
    def longestPalindrome(self, s: str) -> str:
        slen = len(s)
        l1,r1 = 0,0
        maxlen = 0

        for i in  range(slen):
            l2 = r2 = i 
            while l2 >= 0 and r2 < slen and s[l2] == s[r2]:
                clen = r2 - l2 + 1
                if clen > maxlen:
                    l1 = l2
                    r1 = r2  
                    maxlen = clen
                l2 -=1
                r2 +=1

            l2 = i
            r2 = i+1 
            while l2 >= 0 and r2 < slen and s[l2] == s[r2]:
                clen = r2 - l2 + 1
                if clen > maxlen:
                    l1 = l2
                    r1 = r2  
                    maxlen = clen
                l2 -=1
                r2 +=1
            
        return s[l1:r1+1]

                




        