class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ""

        # left should start at 0
        for left in range(n):
            # right should start from left, not fixed at n-1
            for right in range(left, n):
                # slice must include right, so use right+1
                substring = s[left:right+1]

                # check palindrome and update
                if substring == substring[::-1] and len(substring) > len(longest):
                    longest = substring

        return longest
