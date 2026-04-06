class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maximum = max(nums)
        idx = nums.index(maximum)
        nums.sort()
        second = nums[-2] * 2
        if maximum >= second:
            return idx
        else:
            return -1

        