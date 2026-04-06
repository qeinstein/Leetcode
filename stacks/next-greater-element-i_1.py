class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #lineaar search, check for the next element and compare before appending to a created array
        n1 = len(nums1)
        n2 = len(nums2)
        arr = []

        i = 0
        while i < n1:
            found = False
            for j in range(n2):
                if nums1[i] == nums2[j]:
                    #loop from that j to the end first one that's greater, append, else append -1
                    for num in nums2[j+1:]:
                        if num > nums2[j]:
                            arr.append(num)
                            found = True
                            break
                    
                    if not found:
                        arr.append(-1)
                    # arr.append(-1)
                    # if nums2[j+1] < nums1[i]:
                    #     arr.append(-1)
                    # elif nums2[j+1] > nums1[i]:
                    #     arr.append(nums2[j+1])
            i += 1
        return arr
