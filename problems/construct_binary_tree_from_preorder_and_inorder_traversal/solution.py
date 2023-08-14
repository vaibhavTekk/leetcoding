# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder and inorder:
            curr = preorder.pop(0)
            root = TreeNode(curr)
            valindex = inorder.index(curr)
            left= inorder[:valindex]
            right = inorder[valindex+1:]
            root.left = self.buildTree(preorder,left)
            root.right = self.buildTree(preorder,right)
            return root
        return None