class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check all rows
        # Check all columns
        # Check all 3*3 grids

        # First check: all rows
        for r in range(9):
            seen = set()
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        # Second check: all columns
        for c in range(9):
            seen = set()
            for r in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        # Third check: all 3*3 grids
        for box_r in range(0, 9, 3):
            for box_c in range(0, 9, 3):
                seen = set()
                for r in range(box_r, box_r + 3):
                    for c in range(box_c, box_c + 3):
                        if board[r][c] in seen:
                            return False
                        if board[r][c] == ".":
                            continue
                        seen.add(board[r][c])

        return True

        
        