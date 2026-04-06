class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_set = [set() for _ in range(9)]
        cols_set = [set() for _ in range(9)]
        boxes_set = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                id_of_box = (r // 3) * 3 + (c // 3)
                if val in rows_set[r] or val in cols_set[c] or val in boxes_set[id_of_box]:
                    return False

                rows_set[r].add(val)
                cols_set[c].add(val)
                boxes_set[id_of_box].add(val)

        return True

        """
        This guy is more optimal because it is just one pass we are using
        """