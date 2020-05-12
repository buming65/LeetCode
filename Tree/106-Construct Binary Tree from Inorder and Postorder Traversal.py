# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        index_map = collections.defaultdict(int)
        for idx, val in enumerate(inorder):
            index_map[val] = idx
        
        def helper(l, r):
            if l > r or not postorder:
                return
            
            val = postorder.pop()
            root = TreeNode(val)
            
            index = index_map[val]
            
            root.right = helper(index + 1, r)
            root.left = helper(l, index - 1)
            
            
            return root
        
        return helper(0, len(inorder) - 1)