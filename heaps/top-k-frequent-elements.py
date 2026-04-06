class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_of_nums = Counter(nums)
        sorted_items = sorted(count_of_nums.items(), key=lambda x: x[1], reverse=True)
        
        return [num for num, freq in sorted_items[:k]]