class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_counter = Counter(stones)
        count = 0
        for  char in jewels:
            print(char)
            count += stones_counter[char]
        return count