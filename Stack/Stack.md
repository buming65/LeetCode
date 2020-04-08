# Stack

## 739. Daily Temperatures

```
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
```

### Solution 1. Stack

* The stack stores the position of each element.
* From the end to start, if current element is bigger than the last element in the stack, that means all the element before current element will not meet the last element in stack. Because the current one is bigger. So we need to pop the last element until there is a bigger element in the stack.
* And if the stack is not null, then the last element in stack will be answer.

```python
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = []
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            else:
                ans[i] = 0
            stack.append(i)
        return ans
```

