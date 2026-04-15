class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            anagrams = {}

            for word in strs:
                anag = tuple(sorted(word))

                if anag in anagrams: anagrams[anag].append(word)
                else: anagrams[anag] = [word]

            output = [values for values in anagrams.values()]            

            return output
