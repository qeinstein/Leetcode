class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == - (1 << 31) and divisor == -1:
            return (1 << 31) - 1

        negative = (dividend < 0) ^ (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:
            shift = 0
            while dividend >= (divisor << (shift + 1)):
                shift += 1

            result += 1 << shift
            dividend -= divisor << shift

        return -result if negative else result
