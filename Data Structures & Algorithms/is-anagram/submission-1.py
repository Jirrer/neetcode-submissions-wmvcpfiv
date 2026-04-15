class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t): return False

        # dictS = {}
        # dictT = {}

        # for index in range(len(s)):
        #     if s[index] in dictS: dictS[s[index]] += 1
        #     else: dictS[s[index]] = 1

        #     if t[index] in dictT: dictT[t[index]] += 1
        #     else: dictT[t[index]] = 1

        # return dictS == dictT   

        return (sorted(s) == sorted(t))     