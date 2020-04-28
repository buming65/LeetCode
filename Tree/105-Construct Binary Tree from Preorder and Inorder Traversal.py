# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        middle = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:middle+1], inorder[:middle])
        root.right = self.buildTree(preorder[middle+1:], inorder[middle+1:])

        return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
            
        if len(preorder) == 0:
            return None
        
        index_map = collections.defaultdict(int)
        
        for idx, val in enumerate(inorder):
            index_map[val] = idx
            
        def helper(l = 0, r = len(inorder)):
            if l == r:
                return None
            
            temp = preorder[self.pre]
            root = TreeNode(temp)
            
            index = index_map[temp]
            
            self.pre += 1
            
            root.left = helper(l, index)
            root.right = helper(index + 1, r)
            
            return root
        
        self.pre = 0
        root = helper()
        return root