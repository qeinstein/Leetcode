class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1

        i = 0
        while i <= r:   #dont pass the 2's
            if nums[i] == 2:
                nums[i], nums[r] = nums[r] , nums[i] #takes all 2's to the end
                r -= 1
            elif nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i] #takes all 0's to the beginning
                l += 1
                i += 1
            else:
                i += 1 #leave the 1's
        