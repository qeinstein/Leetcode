class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        orig = [row[:] for row in matrix]

        for c in range(n):
            array = []
            for r in range(n-1, -1, -1):
                array.append(orig[r][c])
            matrix[c] = array
        