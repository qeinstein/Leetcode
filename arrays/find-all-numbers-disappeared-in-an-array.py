class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        I should try to solve this guy without extra space
        """
        # another non eone space
        real = set()
        n = len(nums)
        for i in range(1, n+1):
            real.add(i)

        set_numm = set(nums)
        return list(num for num in real if num not in set_numm)
