# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root:
            dq = [root]
            while dq:
                arr = []
                for i in range(len(dq)):
                    curr = dq.pop(0)
                    arr.append(curr.val)
                    if curr.left:
                        dq.append(curr.left)
                    if curr.right:
                        dq.append(curr.right)
                res.append(arr)
        res.reverse()
        return res