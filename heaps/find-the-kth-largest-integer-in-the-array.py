class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        cheat_code = []
        for i in range(len(nums)):
            cheat_code.append(int(nums[i]))

        cheat_code.sort()
        k *= -1
        result = cheat_code[k]
        return str(result)        