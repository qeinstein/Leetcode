class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []

        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = [""]  # start with empty suffix

        for d in reversed(digits):
            letters = mapping[d]
            new = []
            # build every prefix × suffix pair
            for L in letters:
                for suffix in res:
                    new.append(L + suffix)
            res = new

        return res
