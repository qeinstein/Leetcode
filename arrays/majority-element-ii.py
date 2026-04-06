class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count =  Counter(nums)
        k = []
        for num  in count:
            if count[num]> len(nums)//3:
                k.append(num)
        return k
                
        