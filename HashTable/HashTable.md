# Hash Table

## 49. Group Anagrams

```
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
```

### Solution 1. Hash Table

* Set the key as sorted string, value are the strings.

```python
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
```

### Solution 2. Categorize by Count

* Set the key as the position in the alpha list.

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for element in s:
                count[ord(element) - ord('a')] += 1
            result[tuple(count)].append(s)
        return result.values()
```

