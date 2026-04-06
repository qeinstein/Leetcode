from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        possible_max = deque()
        result = []

        for idx, val in enumerate(nums):

            # remove elements that are no longer inside the window
            while possible_max and possible_max[0] < (idx - k + 1):
                possible_max.popleft()

            # Remove elements that are smaller than the current value
            # Since they can never be maximun again
            while possible_max and nums[possible_max[-1]] <= val:
                possible_max.pop()


            # add the current elemeent as a candidate
            possible_max.append(idx)

            if idx >= (k - 1):
                result.append(nums[possible_max[0]])

        return result
        