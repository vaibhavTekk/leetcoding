# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        dq = deque([[p,q]])
        while dq:
            p,q = dq.popleft()
            if not p and not q:
                continue
            if not p or not q:
                return False
            if p.val == q.val:
                dq.append([p.left,q.left])
                dq.append([p.right,q.right])
            else:
                return False
        return True