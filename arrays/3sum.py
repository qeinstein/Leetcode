class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n==3 and sum(nums) != 0:
            return []

        if n ==3 and sum(nums) == 0:
            return [nums]


        
        
        #now for the real deal
        nums.sort()
        #loop through, then the rest is a 2 pointer thuny
        res = set()
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicates for i
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return [list(t) for t in res]
                





        