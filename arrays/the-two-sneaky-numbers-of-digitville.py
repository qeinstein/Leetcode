class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # count = Counter(nums)
        # return [num for num, frequency in count.items() if frequency>=2]

        #let's try a more optimal approach
        result = []
        visited = set()
        
        for num in nums:
            if num in visited:
                result.append(num)
            else:
                visited.add(num)
        return result



        