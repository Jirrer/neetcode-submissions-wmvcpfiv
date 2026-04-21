class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            keyWord = "".join(sorted((word)))

            if keyWord in anagrams: anagrams[keyWord].append(word)
            else: anagrams[keyWord] = [word]


        return [x for x in anagrams.values()]