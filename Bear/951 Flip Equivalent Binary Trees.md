# 951 Flip Equivalent Binary Trees
* Problem:
	* Find the flip equivalent binary trees
* Solution:
	* root -> root.left -> root.right
```
if root == root:
    return True
compare the left node and right node, here are two situation, left == left, right == right. Or left == right, right == left.
The first don't need to flip, the second needs to flip.

if root1 == none or root2 == none or root1 != root2, then is not flip equivalent tree.
```
#Leetcode/problems/tree