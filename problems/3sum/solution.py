class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        array = []
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            a = nums[i]
            while(left < right):
                # print(i,left,right)
                if nums[left] + nums[right] + a > 0:
                    right -= 1
                elif nums[left] + nums[right] + a < 0:
                    left += 1
                else:
                    arr = [nums[i],nums[left],nums[right]]
                    if arr not in array:
                        array.append(arr)
                    left += 1
                    right -= 1
        return array