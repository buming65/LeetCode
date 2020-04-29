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