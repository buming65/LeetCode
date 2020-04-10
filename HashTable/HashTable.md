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

## 438. Find All Anagrams in a String

```
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

### Solution 1. Hash Table

* Each step, delete the last step value that inserted in the array.

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return
        
        p_counter = [0] * 26
        s_counter = [0] * 26
        ans = []
        
        for i in range(len(p)):
            p_counter[ord(p[i])-ord('a')] += 1
        
        for i in range(len(s)):
            s_counter[ord(s[i])-ord('a')] += 1
            if i >= len(p):
                s_counter[ord(s[i-len(p)])-ord('a')] -= 1
            if s_counter == p_counter:
                ans.append(i-len(p)+1)
        return ans 
```

