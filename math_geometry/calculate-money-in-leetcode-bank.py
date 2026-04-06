class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7

        # Sum of full weeks
        total = 28 * weeks + 7 * weeks * (weeks - 1) // 2

        # Sum of remaining days
        start = weeks + 1
        total += days * (2 * start + (days - 1)) // 2

        return total
