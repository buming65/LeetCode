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

## 210. Course Schedule II

```
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
```

### Solution 1. DFS

* `0 not visited, 1 visiting, 2 visited`. If in one traverse, meet the node that is visiting, it indicates that there's a cycle.
* Else, when visited all the adjacent nodes, mark as visited, put into top of the stack

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.courses = collections.defaultdict(list)
        for curr, pre in prerequisites:
            self.courses[pre].append(curr)
        
        stack = []
        visited = [0] * numCourses
        for i in range(numCourses):
            if not self.traverse(visited, stack, i):
                return []
        return stack
        
    def traverse(self, visited, stack, i):
        if visited[i] == 1:
            return False
        if visited[i] == 2:
            return True
        
        visited[i] = 1
        for j in self.courses[i]:
            if not self.traverse(visited, stack, j):
                return False
        visited[i] = 2
        stack.insert(0, i)
        return True
```

