class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        if (list1 != None) and (list2 != None):
            if (list1.val <= list2.val):
                current = list1
                list1 = list1.next
            else:
                current = list2
                list2 = list2.next
            head = current
        elif (list1 != None) and (list2 == None):
            head = list1
            return head
        elif (list1 == None) and (list2 != None):
            head = list2
            return head
        else:
            return head        

        for i in range(1, 100):
            if (list1 != None) and (list2 != None):
                if (list1.val <= list2.val):
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
            elif (list1 != None) and (list2 == None):
                current.next = list1
                break
            elif (list1 == None) and (list2 != None):
                current.next = list2
                break
            else:
                break
            current = current.next
        
        return head