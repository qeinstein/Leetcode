class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        joined_arrays = nums1 + nums2
        joined_arrays.sort()

        length = len(joined_arrays)
        half = int(length//2)
        if length%2 == 1:
            return joined_arrays[half]
        else:
            return (joined_arrays[half - 1] + joined_arrays[half])/2
        