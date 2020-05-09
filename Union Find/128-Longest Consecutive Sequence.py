class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        num_set = set(nums)
        
        for num in num_set:
            if num - 1 not in num_set:
                current = num
                temp = 1
                while current + 1 in num_set:
                    current += 1
                    temp += 1
                
                ans = max(ans, temp)
                    
        return ans


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return parent[x]
        
        def union(x, y):
            xroot, yroot = find(x), find(y)
            if xroot == yroot:
                return
            parent[xroot] = yroot
            rank[yroot] += 1
        
        nums = sorted(set(nums))
        parent = {}
        rank = {}
        for num in nums:
            parent[num] = num
            rank[num] = 1
            if num - 1 in parent:
                union(num, num - 1)
        
        return max(rank.values()) if rank else 0