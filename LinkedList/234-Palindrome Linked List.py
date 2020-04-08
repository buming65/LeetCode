# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        first_end = head
        second_start = head
        
        #Find the second half
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        first_end = slow
        
        #Reverse
        prev = None
        curr = first_end.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        second_start = prev
        
        #Compare
        first_start = head
        while second_start:
            if first_start.val != second_start.val:
                return False
            first_start = first_start.next
            second_start = second_start.next
        
        return True
        