class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if len(nums) == 1:
        #     if nums[0] == target:
        #         return 0
        #     else:
        #         return -1
        #finding pivot
        
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while (left <= right):
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                break
            # print(mid)
        pivot = mid
        # print(pivot)
        #binary search on rotated array
        left = 0
        right = len(nums) - 1
        mid = left + right // 2
        pos = -1
        while(left <= right):
            mid = (left + right) // 2
            realmid = (mid + pivot) % len(nums)
            if nums[realmid] < target:
                left = mid + 1
            elif nums[realmid] > target:
                right = mid - 1
            elif nums[realmid] == target:
                pos = realmid
                break
        return pos
