"""
Prefix sum for 2d arrays basically.
"""

def 2d_prefix_sum(arr):
    # number of rows
    n = len(arr)

    # number of columns
    m = len(arr[0])

    # initlaise prefix with 0s
    prefix = [[0] * m for _ in range(n)]

    # computer prefix sum matrix
    for i in range(n):
        for j in range(m):
            # start with original value
            prefix[i][j] = arr[i][j]

            # add value from top cell if it exists
            if i > 0:
                prefix[i][j] += prefix[i - 1][j]

            # add value from left cell if it exists
            if j > 0:
                prefix[i][j] += prefix[i][j - 1]

            # substract overlap frpm top-left diagonal if it exists
            if i > 0 and j > 0:
                prefix[i][j] -= prefix[i - 1][j - 1]

    return prefix

# example usage
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

if __name__ == "__main__":
    prefix = 2d_prefix_sum(arr)
    for row in prefix:
        print(row)  