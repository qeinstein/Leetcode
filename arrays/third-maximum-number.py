class Solution(object):
    def thirdMax(self, nums):
        num = list(set(nums))
        num.sort()
        if len(num) >= 3:
            return num[-3]
        return num[-1]