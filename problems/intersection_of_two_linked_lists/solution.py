# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        h1 = headA
        len1 = 1
        while h1.next:
            h1 = h1.next
            len1 += 1

        h2 = headB
        len2 = 1
        while h2.next:
            h2 = h2.next
            len2 += 1

        k = abs(len2 - len1)
        if (len2 > len1):
            for i in range(k):
                headB = headB.next
        else:
            for i in range(k):
                headA = headA.next

        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next

        return None