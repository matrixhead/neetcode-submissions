class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjl = {i:[] for i in range(n)}
        for v1,v2 in edges:
            adjl[v1].append(v2)
            adjl[v2].append(v1)
        visited = set()

        def dfs(root, previous):
            if root in visited:
                return False 
            visited.add(root) 
            for c in adjl[root]:
                if c == previous:
                    continue
                if not dfs(c,root):
                    return False
            return True
        
        return dfs(0,-1) and len(visited) == n


            
        