"""
sliding window that it's size changes

a variable-size slidinf window is a fundamentaal algorithmic
pattern used to find an optimal subarray ( or substring) that meets a specific condition

Time: $O(n)$. Even though there is a while loop inside a for loop, each element is visited at most twice: once by the right pointer and once by the left pointer
Space: $O(1)$ for simple sum problems, or $O(K)$ if you are using a Hash Map to track frequencies (common in string problems).
"""


# smallest subarray with given sum 

def smallest_subarray_with_given_sum(target_sum, arr):
    window_sum = 0
    min_length = float('inf')
    left = 0

    # right is the leading pointer
    for right in range(len(arr)):
        window_sum += arr[right]     # add the next element

        #shrink the window as small as possible while window_sum >= target_sum
        while window_sum >= target_sum:
            min_length = min(min_length, right - left + 1)
            window_sum -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else 0



# Example usage:
# arr = [2, 1, 5, 2, 3, 2], target = 7
# Result: 2 (the subarray [5, 2])























