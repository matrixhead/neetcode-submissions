# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root,1)]
        res = 0

        while stack:
            node, lvl = stack.pop()
            if node:
                res = max(res,lvl)
                stack.append((node.left,lvl+1))
                stack.append((node.right,lvl+1))
        
        return res
                
                
       






        