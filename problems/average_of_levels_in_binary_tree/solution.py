# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root:
            stack = [root]
            avg = []
            while stack:
                n = len(stack)
                currsum = 0
                for i in range(n):
                    curr = stack.pop(0)
                    currsum += curr.val
                    if curr.left:
                        stack.append(curr.left)
                    if curr.right:
                        stack.append(curr.right)
                avg.append(currsum/n)
            return avg
        return 0