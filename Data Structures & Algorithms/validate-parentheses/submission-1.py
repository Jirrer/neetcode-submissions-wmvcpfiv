class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charBook = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if c in charBook: stack.append(c)
            else: 
                if len(stack) > 0 and c == charBook[stack.pop()]: continue
                else: return False

        if len(stack) > 0: return False
        else: return True 
        