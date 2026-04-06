from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0
        n = len(nums)

        while True:
            # check if non-decreasing
            sorted_ok = True
            for i in range(n - 1):
                if nums[i] > nums[i + 1]:
                    sorted_ok = False
                    break
            if sorted_ok:
                return ops

            # find leftmost adjacent pair with minimum sum
            min_sum = nums[0] + nums[1]
            idx = 0
            for i in range(1, n - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i

            # merge in place
            nums[idx] = min_sum
            # shift left everything after idx+1
            for j in range(idx + 1, n - 1):
                nums[j] = nums[j + 1]
            nums.pop()

            n -= 1
            ops += 1
