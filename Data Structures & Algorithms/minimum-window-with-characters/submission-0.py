class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, req = {}, {}
        for c in t:
            req[c] = req.get(c,0) + 1
        l = 0
        have, need = 0, len(req)
        residx, reslen = None, float('inf') 
        for r in range(len(s)):
            c = s[r]
            if c in req:
                window[c] = window.get(c,0) + 1
                if window[c] == req[c]:
                    have +=1
            while have == need:
                currentlen = r-l+1
                if reslen > currentlen:
                    residx = [l,r]
                    reslen = currentlen

                lc = s[l]
                if (lc in req) and window[lc] > 0 :
                    window[lc]  = window [lc] - 1
                    if window[lc] < req[lc]:
                        have -=1
                l +=1
        
        return s[residx[0]:residx[1]+1] if residx else ""


        
        

        
        