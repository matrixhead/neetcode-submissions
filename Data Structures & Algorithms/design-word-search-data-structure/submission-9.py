class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.endofword = True
        

    def search(self, word: str) -> bool:

        wlen = len(word)

        def dfs(root:TrieNode,i:int)->bool:
            if wlen == i:
             return root.endofword
            c = word[i]
            if c in root.children:
                return dfs(root.children[c],i+1)
            elif c == ".":
                for child in root.children.values():
                    if dfs(child,i+1):
                        return True
            return False
        
        return dfs(self.root,0)







                     
        
