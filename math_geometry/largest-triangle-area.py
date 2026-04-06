import math

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        largest = 0
        length = len(points)
        for i in range(0, length):   #x1,y1
            for j in range(i+1, length):   #x2,y2
                for k in range(j+1, length):   #x3,y3
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    area = 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

                    largest = max(largest, area)
        return largest
        