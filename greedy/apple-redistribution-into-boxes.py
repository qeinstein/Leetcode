class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort()
        count =0
        summ = 0
        total = sum(apple)
        for i in range(len(capacity)-1, -1, -1):
            summ += capacity[i]
            count += 1

            if summ >= total:
                return count
        