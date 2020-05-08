class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        if not positions:
            return []
        
        self.count = 0
        parent = {}
        res = []
        adjs = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return parent[x]
        
        def union(a, b):
            xroot, yroot = find(a), find(b)
            if xroot == yroot:
                return
            parent[xroot] = yroot
            self.count -= 1
            
        for i, j in positions:
            index = i * n + j
            if index in parent:
                res.append(self.count)
                continue
            self.count += 1
            parent[index] = index
            for adj in adjs:
                x = i + adj[0]
                y = j + adj[1]
                index2 = x * n + y
                if 0 <= x < m and 0 <= y <n and index2 in parent:
                    union(index, index2)
            res.append(self.count)
        
        return res