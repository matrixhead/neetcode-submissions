class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endofword:Optional[str] = None
            

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
            cur.endofword = word
        
        def dfs(root:tuple[int,int], trienode:TrieNode, result: List):
            # check index is valid
            if root[0] == -1 or root[1] == -1:
                return
            if root[0] == ROWS or root[1] == COLUMNS:
                return  
            
            value = board[root[0]][root[1]]

            if value == "#":
                return
            if value not in trienode.children:
                return
            next_t_node  = trienode.children[value]


            if next_t_node.endofword:
                result.append(next_t_node.endofword)
                next_t_node.endofword = None
            
            directions = [[0,1],[1,0],[0,-1],[-1,0]]

            board[root[0]][root[1]] = "#"
            for rdelta, cdelta in directions:
                new_r_index = root[0] + rdelta
                new_c_index = root[1] + cdelta
                new_root = (new_r_index,new_c_index)
                dfs(new_root,next_t_node,result)
            board[root[0]][root[1]] = value

        result = []
        for r in range(ROWS):
            for c in range(COLUMNS):
                dfs((r,c),root,result)

        return result


