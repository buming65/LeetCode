class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        tables = collections.defaultdict(dict)
        
        def dfs(x, y, tables, visited):
            if x == y:
                return 1.0
            visited.add(x)
            for neigh in tables[x]:
                if neigh in visited:
                    continue
                visited.add(neigh)
                d = dfs(neigh, y, tables, visited)
                if d > 0:
                    return d * tables[x][neigh]
            return -1.0
        
        ans = []
        for (x, y), value in zip(equations, values):
            tables[x][y] = value
            tables[y][x] = 1.0 / value
        
        for x, y in queries:
            temp = -1.0
            if x in tables and y in tables:
                temp = dfs(x, y, tables, set())
            ans.append(temp)
        
        return ans 