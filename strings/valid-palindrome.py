class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_m = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return s_m == s_m[::-1]