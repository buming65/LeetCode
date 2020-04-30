# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node:
                return 
            
            if not node.left and not node.right:
                return node
            
            leftSub = dfs(node.left)
            rightSub = dfs(node.right)
            
            if leftSub:
                leftSub.right = node.right
                node.right = node.left
                node.left = None
            return rightSub if rightSub else leftSub
        
        return dfs(root)


