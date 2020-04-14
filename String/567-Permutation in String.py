class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2_counter = [0] * 26
        s1_counter = [0] * 26
        for i in range(len(s1)):
            s1_counter[ord(s1[i])-ord('a')] += 1
        for i in range(len(s2)):
            s2_counter[ord(s2[i])-ord('a')] += 1
            if i >= len(s1):
                s2_counter[ord(s2[i-len(s1)]) - ord('a')] -= 1
            if s1_counter == s2_counter:
                return True
        return False

