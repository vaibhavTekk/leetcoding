"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        return self.traverse(root,[])

    def traverse(self,root,arr):
        if root:
            for i in root.children:
                self.traverse(i,arr)
            arr.append(root.val)
        return arr