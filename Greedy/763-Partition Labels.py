class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {value: index for index, value in enumerate(S)}
        max_index, pivot = 0, 0
        ans = []
        
        for index, value in enumerate(S):
            max_index = max(max_index, last[value])
            if index == max_index:
                ans.append(max_index - pivot + 1)
                pivot = max_index + 1
        
        return ans 