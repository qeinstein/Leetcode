class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        right = len(numbers) - 1
        left = 0

        while right > left:
            sum = numbers[right] + numbers[left]

            if sum == target:
                return [left+1, right+1]
            elif sum < target:
                left+=1
            else:
                right-=1

        return [] 

        