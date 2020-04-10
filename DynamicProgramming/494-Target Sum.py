class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums or sum(nums) < S:
            return 0
        dic = {0:1}
        for i in range(len(nums)):
            temp = collections.defaultdict(int)
            for d in dic:
                temp[d+nums[i]] += dic[d]
                temp[d-nums[i]] += dic[d]
            dic = temp
        return dic[S]