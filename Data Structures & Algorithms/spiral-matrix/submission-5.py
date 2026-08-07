class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = len(matrix)
        c = len(matrix[0])
        nl = min(math.ceil(r/2),math.ceil(c/2))
        res = []
        for i in range(nl):
            r2 = r - (i*2)
            c2 = c -(i*2)
            for c3 in range(c2):
                res.append(matrix[i][i+c3])
            if r2 <= 1:
                continue
            for r3 in range(1,r2):
                res.append(matrix[i+r3][i+c2-1])
            if c2 <= 1:
                continue
            for c3 in range(c2-2,-1,-1):
                res.append(matrix[i+r2-1][i+c3])
            for r3 in range(r2-2,0,-1):
                res.append(matrix[i+r3][i])
        return res
        