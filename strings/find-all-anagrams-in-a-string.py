class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #use sort for the anagram stuff
        #tart from the end indices for the new window
        start_indices = []
        k = len(p)
        n = len(s)
        if n < k:
            return start_indices
        
        countP = Counter(p)
        countS = Counter(s[:k])

        if countS == countP:
            start_indices.append(0)

        for i in range(k,n):
            countS[s[i]] += 1
            countS[s[i-k]] -= 1

            if countS[s[i-k]] == 0:
                del countS[s[i-k]]
            
            if countS == countP:
                start_indices.append(i - k + 1)

        return start_indices