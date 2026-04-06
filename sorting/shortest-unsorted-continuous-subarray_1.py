from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # sliding window for sure

        n = len(nums)

        if (nums == sorted(nums)) or (n == 1):
            return 0

        # --- left scan (maintain strictly increasing indices) ---
        stack_increase = []
        left_idx = n  # will store smallest index that needs sorting

        for i in range(n):
            # push while maintaining increasing order; if violation, pop and record
            while stack_increase and nums[stack_increase[-1]] > nums[i]:
                left_idx = min(left_idx, stack_increase.pop())
            stack_increase.append(i)

        # if no violation found
        if left_idx == n:
            return 0

        leftmost = left_idx

        # --- right scan (maintain strictly decreasing indices from right) ---
        stack_decrease = []
        right_idx = -1  # will store largest index that needs sorting

        for j in range(n - 1, -1, -1):
            # push while maintaining decreasing order; if violation, pop and record
            while stack_decrease and nums[stack_decrease[-1]] < nums[j]:
                right_idx = max(right_idx, stack_decrease.pop())
            stack_decrease.append(j)

        # if no violation found
        if right_idx == -1:
            return 0

        rightmost = right_idx

        # final sanity: if boundaries cross, array is sorted
        if rightmost <= leftmost:
            return 0

        answer = rightmost - leftmost + 1
        return answer
