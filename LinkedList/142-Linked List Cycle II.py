# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        #hash set
        visited = set()
        node = head
        while node:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        return None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def get(self, head):
        tortoise = head
        hare = head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return hare
        return None
    
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return
        start = self.get(head)
        if not start:
            return
        
        start_1 = head
        start_2 = start
        while start_1 != start_2:
            start_1 = start_1.next
            start_2 = start_2.next
        return start_1
        