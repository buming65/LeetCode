class Solution(object):
    def lengthOfLongestSubstring(self, s):
        temp = []
        result = 0

        for word in s:
            if word in temp:
                temp = temp[temp.index(word) + 1:]
            temp.append(word)
            result = max(len(temp),result)
        return result