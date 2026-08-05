class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjlist = {i:[] for i in range(n)}
        for e in edges:
            adjlist[e[0]].append(e[1])
            adjlist[e[1]].append(e[0])

        visited = set()

        def dfs(root,prev):
            if root in visited:
                return 
            visited.add(root)
            for e in adjlist[root]:
                if e == prev:
                    continue
                dfs(e,root)
        res = 0
        for i in range(n):
            if i in visited:
                continue
            res +=1
            dfs(i,-1)
        
        return res
            