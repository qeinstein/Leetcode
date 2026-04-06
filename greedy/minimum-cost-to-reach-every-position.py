class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        # min_num = float('inf')
        n = len(cost)
        output = []

        # for i in range(n):
        #     if cost[i] < min_num:
        #         min_num = cost[i]
        #     output.append(min_num)
        # return output


        #in place modification
        output.append(cost[0])
        for i in range(1, n):
            output.append(min(cost[:i+1]))
        return output



        