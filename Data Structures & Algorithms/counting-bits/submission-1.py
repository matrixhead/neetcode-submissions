class Solution:
    def countBits(self, n: int) -> List[int]:

        res = [0]
        x = 0
        for i in range(1,n+1):
            if (i & i-1) == 0:
                x = 0
            else:
                x +=1
            res.append(res[x]+1)
        
        return res






        