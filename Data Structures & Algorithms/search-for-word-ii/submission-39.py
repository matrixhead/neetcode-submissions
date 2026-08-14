from typing import List, Optional

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word: Optional[str] = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])

        # 1. Build the Trie
        root = TrieNode()
        for w in words:
            cur = root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = w

        # 2. DFS traversal
        def dfs(r: int, c: int, parent: TrieNode, result: List[str]):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] == "#":
                return  
            
            char = board[r][c]
            if char not in parent.children:
                return
                
            curr_node = parent.children[char]

            if curr_node.word:
                result.append(curr_node.word)
                curr_node.word = None 
            
            board[r][c] = "#"
            
            dfs(r + 1, c, curr_node, result)
            dfs(r - 1, c, curr_node, result)
            dfs(r, c + 1, curr_node, result)
            dfs(r, c - 1, curr_node, result)
            
            board[r][c] = char

            # Deep pruning
            if not curr_node.children and not curr_node.word:
                del parent.children[char]

        # 3. Start DFS from every cell
        result = []
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, result)

        return result