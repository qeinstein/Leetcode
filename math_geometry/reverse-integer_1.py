class Solution:

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
        


