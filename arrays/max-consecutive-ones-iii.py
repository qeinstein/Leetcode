class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left =  0
        n  =  len(nums)
        max_a = 0
        zeros = 0
        for right in range(n):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_a = max(max_a, right - left + 1)
        return max_a

        #     count[nums[right]] += 1
        #     window_len = right - left + 1
        #     no_of_ones = nums.count(1)
        #     no_of_zeros = nums.count(0)

        #     while no_of_zeros > k:
        #         count[nums[left]] -= 1
        #         left += 1
        #     max_a = max(max_a, window_len)
        # return max_a

            


        