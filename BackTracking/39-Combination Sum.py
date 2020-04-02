class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def dfs(remain, seq):
            if remain == 0:
                result.append(seq)
                return
            for item in candidates:
                if item > remain:
                    break
                if seq and item < seq[-1]:
                    continue
                else:
                    dfs(remain - item, seq + [item])
        dfs(target, [])
        return result