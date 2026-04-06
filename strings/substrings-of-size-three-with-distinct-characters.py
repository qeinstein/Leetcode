class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        #use sliding window to move for each window check if the characters are unique
        #if it's unique +1 if not continue


        n = len(s)
        count = 0
        for left in range(n-2):
            if len(set(s[left:left+3])) == len(s[left:left+3]):
                count += 1
        return count
        