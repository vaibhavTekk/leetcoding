# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def dfs(self, node, maxval):
        if not node:
            return

        newmax = maxval
        if node.val >= maxval:
            self.count += 1
            newmax = node.val
        if node.right:
            self.dfs(node.right,newmax)
        if node.left:
            self.dfs(node.left,newmax)

    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        self.dfs(root,float('-inf'))
        return self.count


                