"""
Implementing prefix sum in arrays

This guy helps w some Lc questions like 560, 303
"""

def prefix_sum(arr: List[int])-> List[int]:
    n = len(arr)

    # Initialising the prefix sum array
    prefix_sum = [0] * n

    prefix_sum[0] = arr[0] 

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] * arr[i]

    return prefix_sum