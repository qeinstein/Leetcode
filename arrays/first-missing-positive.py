class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numset = set(nums)

        i = 1
        while i in numset:
            i = i + 1
        return i