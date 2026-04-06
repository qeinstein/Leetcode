class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        # left, right = 0, len(nums) - 1
        # nums.sort()
            
        # while left< right:
        #     sum_ = nums[left] + nums[right]

        #     if sum_ == target:
        #         return left, right
        #     elif sum_ < target:
        #         left += 1
        #     else:
        #         right -= 1
        # return []
        