class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def haszero(x: str):
            return '0' not in str(x)

        for i in range(1, n):
            b = n - i

            if haszero(b) and haszero(i):
                return i, b