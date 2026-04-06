class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # First let's define the function to get the time given a val k
        def time_taken(k: int, piles = piles) -> int:
            total_time = 0

            for pile in piles:
                time = ceil(pile/k)
                total_time += time

            return total_time

        # Now a bs on the time shii
        max_pile = max(piles)
        n = len(piles)  # I can use len, it is O(1)
        # The binary search is from range(1, max_pile)
        # we check if the time taken is less than or greater than h then we make changes based on that

        left, right = 1, max_pile

        while left < right:
            mid = left + (right - left) // 2
            t = time_taken(mid)
            if t <= h:
                right = mid
            
            elif t > h:
                left = mid + 1

        return left

        