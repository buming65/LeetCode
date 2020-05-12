# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
    
    def dfs(self, root):
        if not root:
            return True
        
        left, right = self.dfs(root.left), self.dfs(root.right)
        
        if left and right and (not root.left or root.left.val == root.val) and \
    (not root.right or root.right.val == root.val):
            self.ans += 1
            return True
        return False
