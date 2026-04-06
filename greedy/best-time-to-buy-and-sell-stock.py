class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')


        for price in prices:
            if price < min_price:   #making sure that we skip the ones lower than it
                min_price = price
            elif price - min_price > max_profit: #
                max_profit =price - min_price
        return max_profit