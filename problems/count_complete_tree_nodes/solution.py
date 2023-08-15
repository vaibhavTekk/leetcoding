# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root:
            self.count += 1
            self.countNodes(root.left)
            self.countNodes(root.right)
            return self.count
        return 0