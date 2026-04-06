class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        right = k
        ans = float('inf')
        for i in range(len(nums) - k + 1):
            now = nums[right - 1] - nums[i]
            ans = min(ans, now)
            right += 1

        return ans