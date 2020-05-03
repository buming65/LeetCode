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