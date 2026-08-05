# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        print(f"s and f set to {head.val if head else "none"}")
        s = f = head
    
        print("finding first half")
        while f and f.next:
            print(f"f moved to {f.next.next.val if f.next.next else "none"}")
            f = f.next.next
            
            print(f"s moved to {s.next.val }")
            s = s.next
        
        print(f"init second half pointer to {s.next.val if s.next else "null"}")
        sh = s.next
        print("set next of last element in first part to none")
        s.next = None
        print("reversing the second half")
        prev = None
        while sh:
            print(f"current value is {sh.val}")
            print(f"save the current value.next {sh.next.val if sh.next else "null"} to temp")
            temp = sh.next
            print(f"point current value.next to prev {prev.val if prev else "Null"}" )
            sh.next = prev
            print(f"update prev to current value")
            prev = sh
            sh = temp

        to_insert = prev
        fh = head

        while to_insert:
            print("save the prev value of the to insert in temp")
            temp = to_insert.next
            print("save the next value of fh in temp2 ")
            temp2 =fh.next
            print("point current current fh .next to the inserting element")
            fh.next = to_insert
            print("point to insert to next value of fh")
            to_insert.next = temp2
            # break
            print("update fh")
            fh = temp2
            print("update to_insert")
            to_insert = temp
            # break


            




        