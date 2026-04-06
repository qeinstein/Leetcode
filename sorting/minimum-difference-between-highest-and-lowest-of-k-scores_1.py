class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        """
        nums[i] is the score of the ith student

        i can pick the scores of any k students ( k is a number that will be given ) from nums so that
        the diff btw the highest and lowest of the k scores is minimized

        given [1, 2, 3, 4, 5], k = 2
        I can pick any 2 numbers 

        the goal is to pick two numbers that will result in the minimun diff or the highest and lowest then return the min diff
        """

        # sorting should help this
        # i sort, then with negative indexing
        # idx = -1 * k
        nums.sort()

        right = k
        ans = float('inf')
        print(nums)
        for i in range(len(nums) - k + 1):
            now = nums[right - 1] - nums[i]
            ans = min(ans, now)
            right += 1

        return ans

            

        