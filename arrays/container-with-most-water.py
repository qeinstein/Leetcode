class Solution:
    def maxArea(self, height: List[int]) -> int:

        right = len(height) - 1
        left = 0
        max_area = 0

        while right> left:
            if height[right] > height[left]:
                area = height[left]* (right - left)
                left+=1
            elif height[left]> height[right]:
                area = height[right]* (right -left)
                right-=1
            else:  # if height[left] == height[right]
                area = height[left] * (right - left)
                left += 1  # or right -= 1

            if area>max_area:
                max_area = area

        return max_area


        