class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = []
        for word in strs:
            chars = [0] * 26
            for letter in word:
                chars[ord(letter.lower()) - 97] += 1

            freq.append(chars)

        seen = {}
        for index in range(len(strs)):
            temp = tuple(freq[index])
            if temp in seen: seen[temp].append(strs[index])
            else: seen[temp] = [strs[index]]


        output = []
        for x in seen.values():
            output.append(x)

        return output