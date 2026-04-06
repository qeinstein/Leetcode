class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(str(i) for i in digits)) + 1
        num_string = list(str(num))  
        num_num = [int(k) for k in num_string]
        return num_num      

        