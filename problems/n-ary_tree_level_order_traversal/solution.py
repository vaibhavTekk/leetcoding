"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root:
            res = []
            dq = deque([root])
            while dq:
                arr = []
                for i in range(len(dq)):
                    curr = dq.popleft()
                    arr.append(curr.val)
                    for i in curr.children:
                        dq.append(i)
                res.append(arr)
            return res
        return []