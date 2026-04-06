class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        stones_counter = Counter(stones)
        count = 0
        for  char in jewels:
            print(char)
            count += stones_counter[char]
        return count
        """

        # more elegant solution
        """
        # Convert jewels to a set for O(1) average lookup time
        jewels_set = set(jewels)
        
        # Count 1 for every stone that is in the jewels_set
        return sum(1 for stone in stones if stone in jewels_set)
        """

        # the almost most elegant one
        """
        count = 0
        for ch in stones:
            if ch in jewels:
                count += 1

        return count
        """

        # the most elegant
        return sum(map(stones.count, jewels))
