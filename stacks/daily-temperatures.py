from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n  # prefill with 0
        stack = []  # stores indices of temperatures

        for i in range(n-1, -1, -1):
            # pop indices with temperatures <= current temperature
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            # if stack is not empty, next warmer day exists
            if stack:
                answer[i] = stack[-1] - i

            # push current index onto the stack
            stack.append(i)

        return answer
