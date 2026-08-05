# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root=root,lBound=float("-inf"),hBound =float("inf"))
    
    def validate(self, root: Optional[TreeNode], lBound: float, hBound:float)-> bool:
        if not root:
            return True
        
        if root.val <= lBound or root.val >= hBound:
            return False
        
        return self.validate(root.left,lBound=lBound,hBound=root.val) and self.validate(root.right,lBound=root.val, hBound= hBound)
        