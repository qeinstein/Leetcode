class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows==1):
            return s    # If (numRows == 1)... There is no pattern
        n = len(s)
        ans = [[] for i in range(numRows)]      # This guys stores the individal rows
        down, across = True, False      # Initially, we're always going to go down first before going across
        row, i = 0, 0

        while (i < n):
            if (down):
                ans[row].append(s[i])
                row += 1    # We've moved to the next row, so we have to increment
                if (row == numRows):
                    down = False
                    across = True
                    row -= 1        # adding the letters across starts from the one before numRows
            elif (across):
                row -= 1
                ans[row].append(s[i])
                if (row == 0):
                    down = True
                    across = False
                    row = 1
            i += 1

        new_s = ""      # Creating the new letter from the initial "s"
        for i in ans:
            for j in range(len(i)):
                new_s += i[j]

        return new_s

