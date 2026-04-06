class Solution(object):
    def summaryRanges(self, nums):
        ress = []
        if not nums:
            return ress
        start = nums[0]
        end = nums[0]
        for n in nums[1:]:
            if n == end + 1:
                end = n
            else:
                if start == end:
                    ress.append(str(start))
                else:
                    ress.append(str(start) + "->" + str(end))
                start = n
                end = n
        if start == end:
            ress.append(str(start))
        else:
            ress.append(str(start) + "->" + str(end))
        return ress