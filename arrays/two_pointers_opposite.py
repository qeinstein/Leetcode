"""
two pointers from opposite ends
"""

# we can apply that on a function below
# Function to check whether any pair exists
# whose sum is equal to the given target value

def twoSum(arr: List[int], target: int)-> bool:
    # given that the array is sorted
    left, right = 0, len(arr) - 1

    while left < right:
        # compute the sum
        sum = arr[left] + arr[right]

        if sum == target:
            return True
        elif sum < target:
            left += 1
        else:
            right -= 1

    return False


# Test below
arr = [-3, -1, 0, 1, 2]
target = -2

# Call the twoSum function and print the result
if twoSum(arr, target):
    print("true")
else:
    print("false")
