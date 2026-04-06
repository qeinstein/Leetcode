class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #in place hmmm
        #idk what to do
        res = []
        count = 0

        for num in nums:
            if num != 0:
                res.append(num)
            elif num == 0:
                count +=1
        zeros = [0]*count
        res += zeros

        for i, num in enumerate(res):
            nums[i] = num
        




        