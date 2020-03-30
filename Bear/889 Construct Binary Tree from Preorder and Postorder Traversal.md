# 889 Construct Binary Tree from Preorder and Postorder Traversal 
* Preorder:
	* root, left, right
* postorder:
	* left, right, root
* Solution:
	* Let’s say the left branch has L nodes. We know the head node of that left branch is pre[1], but it also occurs last in the postorder representation of the left branch. So pre[1] = post[L-1] (because of uniqueness of the node values.) Hence, L = post.indexOf(pre[1]) + 1. Now in our recursion step, the left branch is represnted by pre[1 : L+1] and post[0 : L], while the right branch is represented by pre[L+1 : N] and post[L : N-1].
```
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        pos = post.index(pre[1]) + 1
        
        root.left = self.constructFromPrePost(pre[1:pos+1], post[:pos])
        root.right = self.constructFromPrePost(pre[pos+1:], post[pos:-1])
        
        return root
```
#Leetcode/problems/tree