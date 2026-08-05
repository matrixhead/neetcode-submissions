class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rlen = len(grid)
        clen = len(grid[0])
        visited = set()

        res = 0

        def bfs(r:int,c:int):
            dq = deque()
            dq.append((r,c))
            i = 0
            while dq:
                root = dq.pop()
                if root in visited or grid[root[0]][root[1]] != "1" :
                    continue
                visited.add(root)
                directions = [(0,1),(1,0),(0,-1),(-1,0)]
                for rd, cd in directions:
                    toappend = ((root[0]+rd),(root[1]+cd))
                    if toappend[0] < 0 or toappend[1]<0 or toappend[0] >= rlen or toappend[1] >= clen:
                        continue
                    dq.append(toappend)


        for r in range(rlen):
            for c in range(clen):
                if (r,c) not in visited and grid[r][c] == "1":
                    bfs(r,c)
                    res +=1
        
        return res


        