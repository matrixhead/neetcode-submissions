# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root,subRoot):
            return True
        
        return (
            self.isSubtree(root=root.left,subRoot=subRoot) or 
            self.isSubtree(root=root.right,subRoot=subRoot))

    def isSameTree(self,treeA:Optional[TreeNode], treeB: Optional[TreeNode]):
        if not treeA and not treeB:
            return True
        if not treeA or not treeB:
            return False
        if treeA.val != treeB.val:
            return False
        
        return self.isSameTree(treeA=treeA.left,treeB=treeB.left) and  self.isSameTree(treeA=treeA.right,treeB=treeB.right)
         