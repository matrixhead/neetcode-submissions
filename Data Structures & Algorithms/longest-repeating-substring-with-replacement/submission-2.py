class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        moc = s[0]
        mocfreq = 1
        freq = {moc:mocfreq}
        res = 0
        for r in range(1,len(s)):
            wlen = r-l+1
            rc = s[r]
            freq[rc] = freq.get(rc,0) + 1
            if mocfreq < freq[rc]:
                moc = rc
                mocfreq  = freq[rc]
            
            while ((wlen - mocfreq) > k) :
                lc = s[l]
                freq[lc] = freq[lc] - 1
                if moc == lc:
                    mocfreq -= 1
                    for ke, va in freq.items():
                        if va > mocfreq:
                            moc = ke
                            mocfreq = va
                l += 1
                wlen = r-l+1
            res = max(wlen,res)
        
        return res



                

        