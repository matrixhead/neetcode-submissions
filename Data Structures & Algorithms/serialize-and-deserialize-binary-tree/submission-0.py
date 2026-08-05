# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(root:Optional[TreeNode], res:List):
            if not root:
                res.append('N')
                return 
            res.append(str(root.val))
            dfs(root=root.left,res=res)
            dfs(root=root.right,res=res)

        res = []
        dfs(root=root,res= res)
        print(res)
        return ",".join(res)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def dfs(vals) -> tuple[Optional[TreeNode],List]:
            root_val = vals[0]
            if root_val == 'N':
                return None,vals[1:]

            res = TreeNode(val=int(root_val))
            res.left,remaining = dfs(vals=vals[1:])
            res.right,remaining = dfs(vals = remaining)

            return res, remaining
        vals = data.split(",")
        tree,_ = dfs(vals)
        return tree
