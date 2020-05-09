class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(1001)]
        
        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return parent[x]
        
        def union(x, y):
            xroot, yroot = find(x), find(y)
            if xroot == yroot:
                return [u, v]
            parent[xroot] = yroot
        
        for u, v in edges:
            if union(u, v):
                return [u, v]
        
        return []