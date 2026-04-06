class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        for i in range(n - 2):
            a, b, c = s[i], s[i+1], s[i+2]
            if a != b and b != c and a != c:
                count += 1

        return count
