# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(L, R):
            if not L and not R:
                return True
            if L and R and L.val == R.val:
                return check(L.left, R.right) and check(L.right, R.left)
            return False
        
        if not root:
            return True
        return check(root.left, root.right)
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = collections.deque([root, root])
        
        while queue:
            t1 = queue.popleft()
            t2 = queue.popleft()
            
            if not t1 and not t2:
                continue
            
            if not t1 or not t2:
                return False
            
            if t1.val != t2.val:
                return False
            
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True
    