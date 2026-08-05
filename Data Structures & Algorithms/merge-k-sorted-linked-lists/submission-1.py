# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or lists[0] is None:
            return None
        while len(lists) != 1:
            new_list = []
            for i in range(0,len(lists),2):
                list_a = lists[i]
                list_b = lists[i+1] if len(lists) > i+1 else None
                merged_list = self.mergeList(list_a=list_a, list_b=list_b)
                new_list.append(merged_list)
            lists = new_list
        return lists[0]
    
    def mergeList(self, list_a: Optional[ListNode],list_b: Optional[ListNode])-> Optional[ListNode]:
        res = ListNode()
        tail = res

        while list_a and list_b:
            value_a = list_a.val
            value_b = list_b.val
            if value_a < value_b:
                print(f"added {value_a}")
                tail.next = list_a
                list_a = list_a.next
            else:
                print(f"added {value_b}")
                tail.next = list_b
                list_b = list_b.next
            tail = tail.next
        
        if list_a:
            tail.next = list_a
        else:
            tail.next = list_b
        
        return res.next

        
        



        