class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return [num for num, frequency in count.items() if frequency>=2]

        