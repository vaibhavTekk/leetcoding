# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            stack = [root]
            res = []
            while stack:
                res.append(stack[-1].val)
                for i in range(len(stack)):
                    curr = stack.pop(0)
                    if curr.left:
                        stack.append(curr.left)
                    if curr.right:
                        stack.append(curr.right)
            return res
        return []
