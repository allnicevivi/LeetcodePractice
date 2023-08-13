# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        add = 0
        ln = ListNode()
        ln_1st = ln
        while (l1 != None) or (l2 != None):
            l1_val = l1.val if l1 != None else 0
            l2_val = l2.val if l2 != None else 0

            val_sum = l1_val + l2_val + add
            if val_sum >= 10:
                add = 1
                ln.val = val_sum - 10
            else:
                add = 0
                ln.val = val_sum
            
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
            
            if (l1 == None) and (l2 == None):
                if add == 1:
                    ln.next = ListNode()
                    ln = ln.next
                    ln.val = add
                else:
                    ln.next = None
            else:
                ln.next = ListNode()
            ln = ln.next
        return ln_1st



