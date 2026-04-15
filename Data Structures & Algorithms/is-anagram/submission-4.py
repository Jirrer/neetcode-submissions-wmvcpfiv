class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = [0] * 26
        letters_t = [0] * 26

        for letter in s:
            letters_s[ord(letter) - 97] += 1

        for letter in t:
            letters_t[ord(letter) - 97] += 1

        return letters_s == letters_t