# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    ListNode.__eq__ = lambda self, other: self.val == other.val
    ListNode.__lt__ = lambda self, other: self.val < other.val
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                node = lists[i]
                heappush(heap,(node.val, node))
        dummy = ListNode()
        temp = dummy
        while heap:
            val, node = heappop(heap)
            newNode = ListNode(val)
            temp.next = newNode
            temp = temp.next
            if node.next:
                heappush(heap,(node.next.val, node.next))

        return dummy.next