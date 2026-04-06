class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        count  = 0
        max_len = 0

        for i in range(len(nums)):
            if nums[i]==1:
                count += 1
            elif nums[i] != 1:
                max_len = max(max_len, count)
                count = 0

        return max(max_len, count)
        