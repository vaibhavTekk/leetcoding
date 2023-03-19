class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ar1 = list()
        ar2 = list()
        flag = -1
        for i in range(len(nums)):
            if (i == 0):
                ar1.append(nums[i])
            else:
                ar1.append(ar1[i-1] + nums[i])
        print(len(nums))
        for i in range(len(nums)-1,-1,-1):
            if (i == len(nums)-1):
                ar2.append(nums[i])
            else:
                ar2.append(ar2[len(ar2)-1] + nums[i])
        for i in range(len(ar1)):
            if ar1[i] == ar2[len(ar1) - i - 1]:
                flag = i
                break
        return flag