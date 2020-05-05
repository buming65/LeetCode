class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, curr = 0, 0
        start_pos = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            curr += gas[i] - cost[i]
            if curr < 0:
                start_pos = i + 1
                curr = 0
        return start_pos if total >= 0 else -1