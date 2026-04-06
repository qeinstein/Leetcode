class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # res = 0
        # for num in nums:
        #     res ^= num
        # return res

        kk = []
        kk2 = []
        for num in nums:
            if num not in kk:
                kk.append(num)
            else:
                kk2.append(num)
        return sum(kk) - sum(kk2)