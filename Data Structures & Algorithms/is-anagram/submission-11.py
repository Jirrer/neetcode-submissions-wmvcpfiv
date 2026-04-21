class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t): return False

        seenS, seenT = {}, {}

        for index in range(len(s)):
            seenT[t[index]] = 1 + seenT.get(t[index], 0)
            seenS[s[index]] = 1 + seenS.get(s[index], 0)

        return seenS == seenT