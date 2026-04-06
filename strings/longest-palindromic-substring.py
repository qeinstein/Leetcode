class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ""

        for center in range(n):
            # Odd-length palindromes
            left, right = center, center
            while left >= 0 and right < n and s[left] == s[right]:
                if (right - left + 1) > len(longest):
                    longest = s[left:right+1]
                left -= 1
                right += 1

            # Even-length palindromes
            left, right = center, center + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if (right - left + 1) > len(longest):
                    longest = s[left:right+1]
                left -= 1
                right += 1

        return longest
