# Back Tracking

## 22. Generate Parentheses

```markdown
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

### Solution 1. Back Tracking

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans
```

* Complexity(Pending)(reference: https://zhuanlan.zhihu.com/p/56693849)
  * Time: 
  * Space: 

### Solution 2. Closure Number(Pending)





## 17. Letter Combinations of a Phone Number

```markdown
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

### Solution 1. Back Tracking

* Store all the conditions for each number as hashmap.
* Back tracking each condition, if no next number, condition satisfy, end.
* Else, add each letter in this number, track next number list.

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }
        
        result = []
        def track(now, next_number):
            if not next_number:
                result.append(now)
            else:
                for letter in number[next_number[0]]:
                    track(now + letter, next_number[1:])
        if digits:
            track("", digits)
        return result
```

* Complexity

  * Time: 
    $$
    O(3^N * 4^M)
    $$
    N is the number of digits maps to 3 letters. M is the number of digits maps to 4 letters.

  * Space: 
    $$
    O(3^N * 4^M)
    $$
    N is the number of digits maps to 3 letters. M is the number of digits maps to 4 letters. Store all the solutions.



## 10. Regular Expression Matching(Pending) 

```
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
```

### Solution 1. Regular Expression 





## 46. Permutations