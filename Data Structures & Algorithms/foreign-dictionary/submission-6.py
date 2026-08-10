class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj = {}
        for word in words:
            for c in word:
                adj[c] = []

        for i in range(1,len(words)):
            first = words[i-1]
            second = words[i]
            for j in range(max(len(first),len(second))):
                if  j==len(second):
                    return ""
                if j == len (first):
                    break
                if first[j] != second[j]:
                    node = adj.get(first[j],[])
                    node.append(second[j])
                    adj[first[j]] = node
                    break

        res = []
        path = set()
        visited = set()

        def dfs(root):
            if root in path:
                return False
            if root in visited:
                return True
            path.add(root)
            node = adj.get(root,[])
            for c in node:
                if not dfs(c):
                    return False
            res.append(root)
            visited.add(root)
            path.remove(root)
            return True
            
        for root in adj.keys():
            if not dfs(root):
                return ""
        
        res.reverse()

        return "".join(res)

                


        