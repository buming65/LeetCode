# Graph

## 207. Course Schedule

```
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
```

### Solution 1. DFS + Topological

* `0` means `not visited`, `1` means `visiting`, `2` means visited.
* First all the node are not visited, when access the node, mark visiting. Visit all the edge from this node. Then mark 2

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course = collections.defaultdict(list)
        for c, p in prerequisites:
            course[p].append(c)
        visited = [0] * numCourses
        for i in range(numCourses):
            if not self.dfs(course, visited, i):
                return False
        return True
    
    def dfs(self, course, visited, i):
        if visited[i] == 1:
            return False
        if visited[i] == 2:
            return True
        visited[i] = 1
        for j in course[i]:
            if not self.dfs(course, visited, j):
                return False
        visited[i] = 2
        return True
```

