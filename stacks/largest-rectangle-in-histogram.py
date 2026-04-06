class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Monotonic mono_stack solution omoh
        """

        mono_stack = []
        max_area = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while mono_stack and heights[mono_stack[-1]] > h:
                height = heights[mono_stack.pop()]
                left = mono_stack[-1] if mono_stack else -1
                width = i - left - 1
                max_area = max(max_area, height * width)
            mono_stack.append(i)

        return max_area