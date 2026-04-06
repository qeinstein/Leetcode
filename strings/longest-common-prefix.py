class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        """
        loop through the array and check if the index of the ftrings are equal rthen append to a string already established
        """

        if not strs:
            return ""

        shortest = min(strs, key=len)
        for i, s in enumerate(shortest):
            for str in strs:
                if str[i] != shortest[i]:
                    return shortest[:i]

        return shortest

            
             

        