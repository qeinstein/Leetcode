"""
We use this guy mostly when we are dealing w a subarray
or things that have to do w consecutive sub-elements in the list
"""


# Sliding window
# Example Problem - Maximum Sum of a Subarray with K Elements
# Given an array arr[] and an integer k, we need to calculate the maximum sum of a subarray having size exactly k.

# Input  : arr[] = [5, 2, -1, 0, 3], k = 3
# Output : 6
# Explanation : We get maximum sum by considering the subarray [5, 2 , -1]

# Input  : arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4 
# Output : 39
# Explanation : We get maximum sum by adding subarray [4, 2, 10, 23] of size 4.

def maxSum(arr: List[int], k: int)-> int:
    # initialise result
    max_sum = float('-inf') # an extremely low number

    for i in range(n - k + 1):
        current_sum = sum(arr[i:i+k-1])
        max_sum = max(current_sum, max_sum)

    return max_sum

if __name__ == "__main__":  # for testinf=g
    arr = [5, 2, -1, 0, 3]
    k = 3
    print(maxSum(arr, k))
