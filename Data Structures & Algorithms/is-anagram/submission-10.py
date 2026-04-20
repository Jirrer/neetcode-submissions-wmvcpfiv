class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        sDict, tDict = {}, {}

        for x in range(len(s)):
            if s[x] in sDict: sDict[s[x]] += 1
            else: sDict[s[x]] = 1

            if t[x] in tDict: tDict[t[x]] += 1
            else: tDict[t[x]] = 1

        return sDict == tDict