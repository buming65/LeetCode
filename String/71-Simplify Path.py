class Solution:
    def simplifyPath(self, path: str) -> str:
        if not str:
            return str
        
        stack = []
        for partition in path.split('/'):
            if partition == "..":
                if stack:
                    stack.pop()
            elif partition == '.' or not partition:
                continue
            else:
                stack.append(partition)
        return "/" + "/".join(stack)