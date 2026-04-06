class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        i, n = 0, len(nums)
        count = 1


        # [1, 1, 2, 3, 3, 3, 3, 4]
        while i < n-1:
            if nums[i] == nums[i+1]:
                count += 1
            else:
                if count > n//2:
                    return nums[i]
                count = 1
            
            i += 1

        return nums[-1]

        