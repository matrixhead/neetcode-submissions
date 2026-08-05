# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        n = 1
        stack:List[TreeNode] = [root]
        cursor = root

        while stack:
            while cursor:
                stack.append(cursor)
                cursor = cursor.left
            
            currentNode = stack.pop()
            if n == k:
                return currentNode.val
            n+=1

            if currentNode.right:
                cursor = currentNode.right

                


        