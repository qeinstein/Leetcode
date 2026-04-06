class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # loop from left to right
        # convert to binary
        # count the one's
        # check if the count is prime
        # if yes, update total

        total = 0

        def is_prime(n: int) -> bool:
            # function to check if a number is prime or not
            # should run in O(1)
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False

            return True


        for i in range(left, right + 1):
            binary = bin(i)[2:] # converted to binary
            ones = binary.count('1')
            if is_prime(ones):
                total += 1
            
        return total