# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root:
            levelorder = []
            stack = [root]
            maxsum = float('-inf')
            maxlevel = 0
            level = 0
            while stack:
                level += 1
                n = len(stack)
                currsum = 0
                for i in range(n):
                    curr = stack.pop(0)
                    currsum += curr.val
                    if curr.left:
                        stack.append(curr.left)
                    if curr.right:
                        stack.append(curr.right)
                if currsum > maxsum:
                    maxsum = currsum
                    maxlevel = level
            return maxlevel
        return 0