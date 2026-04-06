from functools import lru_cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #so basically we're always starting at min(num[0], num[1])

        @lru_cache(None)
        def dfs(i):

            n = len(cost)

            if i >= n:
                return 0
            return cost[i] + min(dfs(i+1), dfs(i+2))

        return min(dfs(0), dfs(1))        