class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        min_num = float('inf')
        n = len(cost)
        output = []

        for i in range(n):
            if cost[i] < min_num:
                min_num = cost[i]
            output.append(min_num)
        return output            

        