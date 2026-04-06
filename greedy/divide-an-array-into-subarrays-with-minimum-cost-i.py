class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # this guy said main issue is figuring out that the first one should always be included
        # but i figured thta out already in < 1min but i stil dont knownwhat to do
        # i can find the next two smallest subarrays
        # space - O(n-1)
        # time - O(n)

        total = 0
        n = len(nums)
        if n < 3:
            return

        total += nums[0]
        space = []
        for i in range(1, n):
            space.append(nums[i])

        space.sort()
        total += space[0]
        total += space[1]

        return total