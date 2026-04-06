class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutation = ["".join(p) for p in permutations(s1)]
        # for perm in permutation:
        #     if perm in s2:
        #         return True
        # return False

        #above exceeds time limit

        #sliding window below
        left = 0
        count1 = Counter(s1)
        count2 = Counter(s2)
        length = len(s2)
        right = len(s1) - 1  # window of size len(s1)

        while right < length:  # move window forward
            while left <= right:  # inner loop checks current window
                count2 = Counter(s2[left:right+1])  # substring of size len(s1)
                if count2 == count1:
                    return True
                break  # only need to check this window once, then move window
            left += 1
            right += 1
        return False



        