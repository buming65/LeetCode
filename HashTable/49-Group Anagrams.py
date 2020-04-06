class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for word in strs:
            key = tuple(sorted(list(word)))
            # print(key)
            if key not in d:
                d.setdefault(key, [])
            d[key].append(word)
        return d.values()

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for element in s:
                count[ord(element) - ord('a')] += 1
            result[tuple(count)].append(s)
        return result.values()