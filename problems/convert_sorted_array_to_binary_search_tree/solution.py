# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        mid = n//2
        midval = nums[mid]
        left,right = self.split(nums,midval)
        root = TreeNode(midval)
        if left:
            root.left = self.sortedArrayToBST(left)
        if right:
            root.right = self.sortedArrayToBST(right)
        return root

    # def helper(self,nums):
    def split(self,nums,val):
        left = []
        right = []
        for i in range(len(nums)):
            if nums[i] < val:
                left.append(nums[i])
            if nums[i] > val:
                right.append(nums[i])
        return left,right
