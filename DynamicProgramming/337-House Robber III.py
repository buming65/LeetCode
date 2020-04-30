# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        
        def dfs(node):
            if not node:
                return 0, 0
            prev_left, curr_left = dfs(node.left)
            prev_right, curr_right = dfs(node.right)
            
            return curr_left + curr_right, max(curr_left + curr_right, node.val + prev_left + prev_right)
        
        return max(dfs(root))