class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # loop from left to right
        # convert to binary
        # count the one's
        # check if the count is prime
        # if yes, update total

        total = 0

        primes = {2, 3, 5, 7, 11, 13, 17, 19}   # number of numbers cant be greater than 8 according to the constraint so we do not need a helper to check for primes


        for i in range(left, right + 1):
            binary = bin(i)[2:] # converted to binary
            ones = binary.count('1')
            if ones in primes:
                total += 1
            
        return total