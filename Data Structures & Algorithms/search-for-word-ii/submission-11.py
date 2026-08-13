class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endofword = False
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self,word:str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endofword = True
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLUMNS = len(board[0])

        root = TrieNode()
        
        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.endofword = True
        
        def dfs(root:tuple[int,int], trienode:TrieNode, path:Set)-> List:
            result = []
            # check index is valid
            if root[0] == -1 or root[1] == -1:
                return result
            if root[0] == ROWS or root[1] == COLUMNS:
                return result
            value = board[root[0]][root[1]]

            if value not in trienode.children:
                return result
            next_t_node  = trienode.children[value]


            if next_t_node.endofword:
                result.append(value)
            
            directions = [[0,1],[1,0],[0,-1],[-1,0]]

            path.add(root)
            
            for rdelta, cdelta in directions:
                new_r_index = root[0] + rdelta
                new_c_index = root[1] + cdelta
                new_root = (new_r_index,new_c_index)
                if new_root in path:
                    continue
                c_results = dfs(new_root,next_t_node,path)
                for cr in c_results:
                    result.append(f"{value}{cr}") 
            path.remove(root)
            return result

        ret = set()
        for r in range(ROWS):
            for c in range(COLUMNS):
                results = dfs((r,c),root,set())
                for result in results:
                    ret.add(result)
        return list(ret)


