class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #i cannot keep count
        count = Counter(nums)
# count is a dict
        return [num for num, freq in count.items() if freq > 1][0]
        