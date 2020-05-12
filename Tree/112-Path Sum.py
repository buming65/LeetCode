# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        queue = [(root, sum - root.val)]
        while queue:
            node, curr = queue.pop()
            if not node.left and not node.right and curr == 0:
                return True
            if node.right:
                queue.append((node.right, curr-node.right.val))
            
            if node.left:
                queue.append((node.left, curr - node.left.val))
        
        return False