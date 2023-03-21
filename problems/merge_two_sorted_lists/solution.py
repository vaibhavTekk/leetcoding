# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        new = None
        if(list1 is None):
            return list2

        if(list2 is None):
            return list1

        if (list1.val < list2.val):
            new = list1
            new.next = self.mergeTwoLists(list1.next,list2)
        else:
            new = list2
            new.next = self.mergeTwoLists(list1,list2.next)

        return new