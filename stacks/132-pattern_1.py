class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        min_i = [0] * n
        min_i[0] = nums[0]
        for i in range(1, n):
            min_i[i] = min(min_i[i-1], nums[i])

        stack = []  # holds potential "2"s
        for j in range(n-1, -1, -1):
            if nums[j] > min_i[j]:
                while stack and stack[-1] <= min_i[j]:
                    stack.pop()
                # If top of stack < nums[j], we found 132
                if stack and stack[-1] < nums[j]:
                    return True
                # Push current number as potential "2" for future
                stack.append(nums[j])
        return False
