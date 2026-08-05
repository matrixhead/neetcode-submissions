# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(val=preorder[0])
        rootidx = inorder.index(preorder[0])

        root.left = self.buildTree(preorder=preorder[1:rootidx+1],inorder=inorder[:rootidx])
        root.right = self.buildTree(preorder=preorder[rootidx+1:],inorder=inorder[rootidx+1:])

        return root

        