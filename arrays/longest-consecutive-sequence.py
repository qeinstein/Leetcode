class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #we cannot sort because of O(n)
        if not nums:
            return 0
        hash_set  = set() #{}
        
        for num in nums:
            hash_set.add(num)
        counts = []


        for num in hash_set:
            curr = num
            count = 1
            if curr - 1 in hash_set:
                continue
            else:
                while curr+1 in hash_set:
                    count += 1
                    curr += 1
                
            counts.append(count)
        # print(max(counts))
        return max(counts)