class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count, t_count = {}, {}

        for index in range(len(s)):
            s_letter = s[index]

            if s_letter in s_count: s_count[s_letter] += 1
            else: s_count[s_letter] = 1

        for index in range(len(t)):
            t_letter = t[index]

            if t_letter in t_count: t_count[t_letter] += 1
            else: t_count[t_letter] = 1

        return s_count == t_count