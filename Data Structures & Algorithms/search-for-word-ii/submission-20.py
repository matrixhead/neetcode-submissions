class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endofword = False
            

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
        
        def dfs(root:tuple[int,int], trienode:TrieNode, path:Set, matched:str, result: Set):
            # check index is valid
            if root[0] == -1 or root[1] == -1:
                return
            if root[0] == ROWS or root[1] == COLUMNS:
                return  
            
            value = board[root[0]][root[1]]

            if value not in trienode.children:
                return
            next_t_node  = trienode.children[value]

            matched = f"{matched}{value}"

            if next_t_node.endofword:
                result.add(matched)
            
            directions = [[0,1],[1,0],[0,-1],[-1,0]]

            path.add(root)
            
            for rdelta, cdelta in directions:
                new_r_index = root[0] + rdelta
                new_c_index = root[1] + cdelta
                new_root = (new_r_index,new_c_index)
                if new_root in path:
                    continue
                dfs(new_root,next_t_node,path,matched,result)
            path.remove(root)
        result = set()
        for r in range(ROWS):
            for c in range(COLUMNS):
                dfs((r,c),root,set(),"",result)
        return list(result)


