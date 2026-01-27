"""
A difference array is basically an auxilliary array that
multiple range update operations efficiently.

Given an original array A, its difference array D is def
element D[i] stores the difference between A[i] and A[i-

A[0] == D[0]
D[i] = A[i] - A[i - 1] (for i > 0)

The "magic" property here is that the prefix sum of the 
up to index "i" gives you the original value A[i]:
"""


# Difference Array exists in higher dimensions
# It extends to 2D, which is useful for image processing

# In 2D a ramge update on a rectagle (x1, y1) to (x2, y2
# in  the 2D Difference array to manage the area boundar

# Example Walkthrough
# If A = [10, 10, 10, 10, 10] and you want to add 5 to i

# 1.. D = [10, 0, 0, 0, 0, 0]
# 2.. Update D[1] += 5 -> [10, 5, 0, 0, 0, 0]
# 3.. Update D[4] -= 5 -> [10, 5, 0, 0, -5, 0]
# 4.. Prefix Sum: [10, (10+5), (10+5+0), (10+5+0+0), (10
# 5.. Result: [10, 15, 15, 15, 10].


# Apply a single range update on the differnece array
def update(diff, left, right, x):
    diff[left] += x
    if right + 1 < len(diff):
        diff[right + 1] -= x

# apply range updates using difference array technique
def diffArray(arr, opr):
    n =len(arr)


    # create difference array
    diff = [0] * n

    # apply each operation [l, r, val] on the diff array
    for left, right, val in opr:
        update(diff, left, right, val)
    
    # build the result by applying prefix sum over diff
    res = arr[:]
    res[0] += diff[0]
    for i in range(1, n):
        diff[i] += diff[i - 1]
        res[i] += diff[i]

    return res

if __name__ = "__main__":
    arr = [1, 2, 3, 4, 5]
    opr = [[1, 3, 10], [2, 4, -5]]

    res = diffArray(arr, opr)

    for num in res:
        print(num, end=" ")
    print()


# this is not  very complicated