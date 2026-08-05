# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        result_tail = result
        while True:
            to_append = None
            if list1 is None and list2 is None:
                break
            elif list1 is None:
                to_append =  list2
                list2 = None
            elif list2 is None:
                to_append = list1
                list1 = None
            else:
                if list1.val < list2.val:
                    to_append = list1
                    list1 = list1.next
                else:
                    to_append = list2
                    list2 = list2.next
            if result_tail:
                result_tail.next = to_append
            else:
                result = to_append
            result_tail = to_append
        return result 
                

            
        