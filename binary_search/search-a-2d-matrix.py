class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_columns = len(matrix[0])
        row = 0
        if not matrix:
            return False

        i=0
        while i < num_rows:
            if matrix[i][num_columns-1] > target:
                row = i
                break
            elif matrix[i][num_columns-1] == target:
                return True
            i += 1
        
        #we've gotten the row our target is
        for t in range(num_columns):
            if target == matrix[row][t]:
                return True
        return False

        
        