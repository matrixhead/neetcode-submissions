class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        freq2 = {}
        for c in s:
            freq[c] = freq.get(c,0) + 1
        
        for c in t:
            freq2[c] = freq2.get(c,0) +1
        
        for key,v in freq.items():
            if v != freq2.pop(key,0):
                return False
        if freq2:
            return False
        
        return True



        