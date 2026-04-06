class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles  # You drink all initial bottles
        empty = numBottles  # Now you have that many empty bottles

        while empty >= numExchange:
            # Exchange as many as possible
            new_full = empty // numExchange
            total += new_full  # Drink these new bottles
            empty = new_full + (empty % numExchange)  # New empties + leftover
        return total
