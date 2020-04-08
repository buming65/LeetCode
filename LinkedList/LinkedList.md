# Linked List

## 160. Intersection of Two Linked Lists

### [Instruction][https://leetcode.com/problems/intersection-of-two-linked-lists/]

### Solution 1. Two Pointers

* I think it's fast and slow pointer which could decided if there is a cycle.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return
        A = headA
        B = headB
        
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
            
```

## 234. Palindrome Linked List

```
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
```

### Solution 1. 