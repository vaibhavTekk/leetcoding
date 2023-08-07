# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        def calcSum(node,val):
            if not node:
                return val
            else:
                return calcSum(node.next,val*2+node.val)

        return calcSum(head,0)