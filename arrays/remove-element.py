class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        n = len(nums)
        for num in nums:
            if num == val:
                count += 1
            else:
                continue

        while val in nums:
            nums.remove(val)
        # nums = [num for num in nums if num != val]
        # nums += [3]*count
        k = n - count
        return k
        