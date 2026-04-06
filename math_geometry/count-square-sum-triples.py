import math 

class Solution:
    def countTriples(self, n: int) -> int:
        #loop through all possible combinations and  check if the sqrt is an integer and if the sqrt is <= 10
        # left = 1
        # right = 0

        count  = 0
        squares = {i**2 for i in range(1, n+1)}
        nos = {i for i in range(1, n+1)}
        for i in range(1, n+1):
        #loop for left
            for j in range(i+1, n+1):
                square = i**2 + j**2
                square_root=square**0.5

                if square_root<= n and square_root in nos:
                    count+=2

                # else:
                #     continue

                # left += 1

        print(count)

        return count


        