# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        
        return max(left_height, right_height) + 1
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = []
        depth = 0
        queue.append(root)
        while queue:
            depth += 1
            for i in range(len(queue)):
                temp = queue.pop(0)
                if temp.left: queue.append(temp.left)
                if temp.right: queue.append(temp.right)
        return depth
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = []
        if not root:
            return 0
        else:
            stack.append((1, root))
            
        depth = 0
        while stack != []:
            cur_depth, node = stack.pop()
            if node:
                depth = max(depth, cur_depth)
                stack.append((cur_depth+1, node.left))
                stack.append((cur_depth+1, node.right))
            
        return depth