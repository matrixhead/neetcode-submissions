# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        t = head
        h = head 
        while t and h and h.next and h.next.next:
            h = h.next.next
            t = t.next
            if t == h:
                return True
        return False

        