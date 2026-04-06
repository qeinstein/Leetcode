class Solution:
    def mySqrt(self, x: int) -> int:

        right = x
        left = 1
        num = 0
        

        while left  <= right:
            mid =(left + right)//2
            if mid * mid <= x:
                num = mid
                left = mid + 1
            else:
                right = mid - 1

        return num
                
        