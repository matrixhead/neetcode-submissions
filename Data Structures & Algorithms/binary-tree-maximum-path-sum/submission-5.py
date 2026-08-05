# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 #unreachable
        resWSplit,resWoSplit = self.dfs(root=root)
        return  max(resWSplit,resWoSplit)
        
    
    def dfs(self,root:TreeNode) -> tuple[int,int]:
        
        val = root.val
        lWSplit,lWoSplit = self.dfs(root.left) if root.left else (None,None)
        rWSplit,rWoSplit = self.dfs(root.right) if root.right else (None,None)

        resWSplit = val+ (lWoSplit if lWoSplit else 0) + (rWoSplit if rWoSplit else 0)

        resWSplit = max(val,resWSplit)
        
        resWSplit = max(resWSplit,lWSplit) if lWSplit else resWSplit

        resWSplit = max(resWSplit,rWSplit) if rWSplit else resWSplit

        resWoSplit = max((val + (lWoSplit if lWoSplit else 0)),(val + (rWoSplit if rWoSplit else 0)), val)


        print(f"entered with {root.val} and returned {resWSplit} {resWoSplit}")
        return (resWSplit, resWoSplit)



        