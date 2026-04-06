class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        no_cols = len(encodedText)//rows
        # basically we're trying to get the original text back
        # we need to build the matrix w the text and then traverse it
        matrix = [[' ' for _ in range(no_cols)] for _ in range(rows)]

        # now to build the matrix w the encoded text
        # for each of those texts, we append it to a column cell in the matrix
        index = 0

        for i in range(rows):
            for j in range(no_cols):
                matrix[i][j] = encodedText[index]
                index += 1

        # the matrix has been built
        # to traverse it and return the result
        # increase row by one and col by 1, when we get to the last row
        # return to the top row after the initial first row and do the same
        string = []

        # row is increasing by 1, col by 1 till row is up
        for j in range(no_cols):
            for i in range(rows):

                c = j + i

                if c >= no_cols:
                    break

                string.append(matrix[i][c])

        return "".join(string).rstrip()





