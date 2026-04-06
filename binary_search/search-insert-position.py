class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                return i

        for i in range(n):
            if nums[i] > target:
                if i == 0:
                    return 0
                else:
                    return i
            elif target > nums[n-1]:
                return n
                



        