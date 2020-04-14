# String

## 567. Permutation in String

```
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
```

### Solution 1. Array

* Use array

```python
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
```

## 3. Longest Substring Without Repeating Characters

```
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

### Solution 1. Sliding Window

* if word appear twice, remove the first word, to the end.
* Compare with the result

```python
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
```

## 14. Longest Common Prefix

```
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
```

### Solution 1. Scanning

```python
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
```

## 43. Multiply Strings

```
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
```

### Solution 1.

```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res, m, n = 0, len(num1), len(num2)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                res += int(num1[-i]) * int(num2[-j]) * 10 ** (i + j - 2)
        return str(res)

```

## 151. Reverse Words in a String

```
Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Follow up:

For C programmers, try to solve it in-place in O(1) extra space.
```

### Solution 1.

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
```

## 71. Simplify Path

```
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level.

Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.

 

Example 1:

Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
Example 4:

Input: "/a/./b/../../c/"
Output: "/c"
Example 5:

Input: "/a/../../b/../c//.//"
Output: "/c"
Example 6:

Input: "/a//b////c/d//././/.."
Output: "/a/b/c"
```

### Solution 1. Stack

* Use stack

```python
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
```

