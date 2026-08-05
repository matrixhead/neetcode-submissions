class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {i:[] for i in range(numCourses)}
        for a,b in prerequisites:
            adjlist[a].append(b)
        
        path = set()
        def dfs(root)->bool:
            prereq = adjlist[root]
            if len(prereq) == 0:
                return True
            if root in path:
                return False
            
            path.add(root)
            for p in prereq:
               if not dfs(p):
                    path.remove(root)
                    return False            
            path.remove(root)
            adjlist[root] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        



        