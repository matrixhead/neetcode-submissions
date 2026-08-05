# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow_p = dummy
        fast_p  = head

        while n != 0 and fast_p:
            fast_p = fast_p.next
            n -= 1
        
        print(f"fast_p moved to {fast_p.val if fast_p else None}")

        while slow_p and fast_p:
            fast_p = fast_p.next
            slow_p = slow_p.next
        
        if slow_p and slow_p.next:
            slow_p.next = slow_p.next.next
        
        print(f"slow_p at {slow_p.val if slow_p else None}")
        print(f"fast_p at {fast_p.val if fast_p else None}")

        return dummy.next

        