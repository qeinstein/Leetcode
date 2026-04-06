class Solution:
    def mySqrt(self, x: int) -> int:

        for i in range(x+1):
            if i * i == x:
                return i
                break
            elif i * i > x:
                return i - 1
        
        

        # right = x
        # left = 1
        # num = 0
        

        # while left  <= right:
        #     mid =(left + right)//2
        #     if mid * mid <= x:
        #         num = mid
        #         left = mid + 1
        #     else:
        #         right = mid - 1

        # return num
                
        