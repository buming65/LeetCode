class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        result = ''
        mi = min([len(s) for s in strs])
        for i in range(mi):
            temp = set([s[i] for s in strs])
            if len(temp) == 1:
                result += strs[0][i]
            else:
                break
        return result