class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = collections.defaultdict(int)
        for task in tasks:
            dic[task] += 1
        
        max_val = max(dic.values())
        
        total = (max_val-1) * (n + 1)
        for key, value in dic.items():
            if value == max_val:
                total += 1
        return max(total, len(tasks))

