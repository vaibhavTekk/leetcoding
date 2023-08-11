# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:    
        dummy = ListNode(0,None)
        new = dummy
        carry = 0
        while l1 and l2:
            new.next = ListNode((l1.val + l2.val + carry)%10,None)
            new = new.next
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
        while l1:
            new.next = ListNode((l1.val + carry)%10,None)
            carry = (l1.val + carry) // 10
            new = new.next
            l1 = l1.next
        while l2:
            new.next = ListNode((l2.val + carry)%10,None)
            carry = (l2.val + carry) // 10
            new = new.next
            l2 = l2.next
        if carry:
            new.next = ListNode(1,None)

        return dummy.next