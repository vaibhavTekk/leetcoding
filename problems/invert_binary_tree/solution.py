# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            nodes = [root]
            while (len(nodes) > 0):
                currnode = nodes.pop()
                if (currnode.right):
                    nodes.append(currnode.right)
                if (currnode.left):
                    nodes.append(currnode.left)
                currnode.left, currnode.right = currnode.right, currnode.left
        return root