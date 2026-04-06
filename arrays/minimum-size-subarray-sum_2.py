class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')  # same as INT_MAX in C++

        for right in range(len(nums)):
            current_sum += nums[right]  # expand window

            # shrink window from the left while the sum condition holds
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return 0 if min_length == float('inf') else min_length
