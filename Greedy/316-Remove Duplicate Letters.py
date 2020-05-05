class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last = {value:index for index, value in enumerate(s)}
        
        for index, value in enumerate(s):
            if value not in stack:
                while stack and value < stack[-1] and index < last[stack[-1]]:
                    stack.pop()
                stack.append(value)
        return "".join(stack)
        
