# 输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。 
# 
#  
# 
#  例如，给出 
# 
#  前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7] 
# 
#  返回如下的二叉树： 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  
# 
#  限制： 
# 
#  0 <= 节点个数 <= 5000 
# 
#  
# 
#  注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-
# preorder-and-inorder-traversal/ 
#  Related Topics 树 递归


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    #Solution 1.
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None

        self.index_map = collections.defaultdict(int)

        for index, value in enumerate(inorder):
            self.index_map[value] = index

        self.pre = 0

        def helper(l, r):
            if l == r:
                return

            temp = preorder[self.pre]
            root = TreeNode(temp)

            self.pre += 1
            index = self.index_map[temp]

            root.left = helper(l, index)
            root.right = helper(index+1, r)

            return root

        root = helper(0, len(inorder))
        return root

# leetcode submit region end(Prohibit modification and deletion)
