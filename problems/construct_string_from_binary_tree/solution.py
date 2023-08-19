# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    string = ''
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.dfs(root)
        return self.string
    def dfs(self,node):
        if node:
            self.string += str(node.val)
            if node.left:
                self.string += '('
                self.dfs(node.left)
                self.string += ')'
            if node.right:
                if not node.left:
                    self.string += '()'
                self.string += '('
                self.dfs(node.right)
                self.string += ')'
            return
        return