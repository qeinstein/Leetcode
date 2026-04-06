from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        length_of_s = len(s)
        left = 0
        right = 0
        substring = ""
        min_len = float("inf")

        # count characters in t
        target_count = Counter(t)
        window_count = {}
        have, need = 0, len(target_count)

        while right < length_of_s:
            ch = s[right]
            window_count[ch] = window_count.get(ch, 0) + 1

            # check if this character count matches target
            if ch in target_count and window_count[ch] == target_count[ch]:
                have += 1

            # when we have all needed characters, try to shrink from left
            while have == need:
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    substring = s[left:right + 1]

                # remove leftmost char and shrink window
                window_count[s[left]] -= 1
                if s[left] in target_count and window_count[s[left]] < target_count[s[left]]:
                    have -= 1
                left += 1

            right += 1

        return substring
