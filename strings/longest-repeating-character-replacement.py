class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #i need to use the count stuff
        #the one with the least frequest count wil be taken, if it's less than <= k the window is valid

        left = 0
        n = len(s)
        countS = Counter()
        max_subs = 0

        for right in range(n):
            countS[s[right]] += 1
            window_length = right - left + 1
            
            most_common = max(countS.values())

            required_changes = window_length - most_common

            while required_changes > k:
                countS[s[left]] -= 1
                left  += 1
                window_length = right - left + 1
                most_common = max(countS.values())
                required_changes = window_length - most_common

            max_subs = max(max_subs, window_length)

        return max_subs

            