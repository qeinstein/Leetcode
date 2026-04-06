class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]

        print(binary)
        last_one = None
        max_gap = 0 
        for i in range(len(binary)):
            if binary[i] == '1':
                if last_one is not None:
                    max_gap = max(max_gap, i - last_one)

                last_one = i
        
        return max_gap
            
        