
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {c: i for i, c in enumerate(s)}  # last occurrence of each character
        stack = []
        seen = set()  # to track characters already in stack

        for i, c in enumerate(s):
            if c in seen:
                continue  # skip duplicates

            # pop characters that are bigger than current and appear later
            while stack and stack[-1] > c and last_index[stack[-1]] > i:
                removed = stack.pop()
                seen.remove(removed)

            stack.append(c)
            seen.add(c)

        return "".join(stack)