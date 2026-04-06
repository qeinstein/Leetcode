class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word)) # we're sorting the word to get a common key for anagram words
            groups[key].append(word) # appending a word to the column of its key

        return list(groups.values())
        