class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rlen = len(heights)
        clen = len(heights[0])
        pacific = set()
        atlantic = set()


        def dfs(r:int, c:int,visited:Set, previous_height:int):
            if (
                r<0 
                or c<0 
                or r>= rlen 
                or c>= clen 
                or (r,c) in visited 
                or heights[r][c] < previous_height
            ):
                return
            visited.add((r,c))
            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            for rd,cd in directions:
                dfs(r+rd,c+cd,visited,heights[r][c])
        
        for c in range(clen):
            dfs(0,c,pacific,0)
            dfs(rlen-1,c,atlantic,0)

        for r in range(rlen):
            dfs(r,0,pacific,0)
            dfs(r,clen-1,atlantic,0)
        return list(pacific.intersection(atlantic))
            
        