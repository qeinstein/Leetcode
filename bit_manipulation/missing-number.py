class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = int(len(nums))
        real_sum = (n*(n+1))//2
        return real_sum - sum(nums) #brute force approach
        