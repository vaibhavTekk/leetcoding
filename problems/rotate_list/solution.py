# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        length = 1
        p = head
        while p.next:
            p = p.next
            length += 1
        p.next = head

        p2 = head
        for i in range(length - (k % length) - 1):
            p2 = p2.next

        newhead = p2.next
        p2.next = None
        
        return newhead