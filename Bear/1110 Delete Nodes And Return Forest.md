# 1110 Delete Nodes And Return Forest 
* Problem:
	* if node in to_delete, delete, then return the forest
* Solution:
```
root, left, right 
First DFS,
if not root:
    return FALSE 
if dfs(left):
    left == none
if dfs(right):
    right == none
if root in delete:
    if left:
        result.append(left)
    if right:
        result.append(right)
    return True #means the root need to be deleted
else:
    return FALSE  
if the root is false which is not be deleted:
    result.append(root)
```
#Leetcode/problems/tree#