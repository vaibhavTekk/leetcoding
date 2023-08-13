# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1,None)
        p = dummy
        while head:
            carry , val = (head.val*2)//10, (head.val*2)%10
            if p.val == -1 and carry != 0:
                p.next = ListNode(carry,None)
                p.next.next = ListNode(val,None)
                p = p.next.next
            else:
                p.val = p.val + carry
                p.next = ListNode(val,None)
                p = p.next
            head = head.next
        return dummy.next
            
        