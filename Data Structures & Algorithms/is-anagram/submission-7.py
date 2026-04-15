class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS, dictT = {}, {}

        for x in s:
            if x in dictS: dictS[x] += 1
            else: dictS[x] = 1

        for x in t:
            if x in dictT: dictT[x] += 1
            else: dictT[x] = 1

        return dictS == dictT
        