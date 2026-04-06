class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        total = 0

        negative_count = 0
        smallest_val = float('inf')
        zero_in  = False

        for mat in matrix:
            for m in mat:
                total += abs(m)
                if m < 0:
                    negative_count += 1
                elif m == 0:
                    zero_in = True
                smallest_val = min(smallest_val, abs(m))

        if negative_count % 2 == 0 or zero_in:
            return total
        
        return total - (2 * smallest_val)