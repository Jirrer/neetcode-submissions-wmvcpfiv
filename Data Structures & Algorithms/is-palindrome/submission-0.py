class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsedStr = ""
        for x in s:
            if x.isalnum(): parsedStr += x.lower()

        for x in range(len(parsedStr) // 2):
            if parsedStr[x] != parsedStr[(len(parsedStr) - 1) - x]: return False
        
        return True
        