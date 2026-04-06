class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = list(set(nums1))
        set2 = list(set(nums2))

        return [num for num in set1 if num in set2]
        