class Solution:
    def is_useful(x: int):
        if -2**31<=x and x <=2**31 -1:
            return True
        else:
            return False
    def reverse(self, x: int) -> int:
        if x< 0:
            sig = -1
            absolute = str(abs(x))
            string = absolute[::-1]
            ans = sig * int(string)
            if -2**31<=ans and ans <=2**31 -1:
                return ans
            else:
                return 0
        elif x > 0 and x%10 != 0:
            abso = str(x)
            ans = int(abso[::-1])
            if -2**31<=ans and ans <=2**31 -1:
                return ans
            else:
                return 0
        else:
            sg = str(x)
            ans = int(sg[::-1])
            if -2**31<=ans and ans <=2**31 -1:
                return ans
            else:
                return 0
        


"""
list out the numbers remove those not in 1 -9 and reverse the rest
check if the end if zero
check if the beginning is -1
those are the two edge cases

if this nonsense i am doing works, then we will r=try iusing str
"""