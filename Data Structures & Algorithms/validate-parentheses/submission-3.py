class Solution:
    def isValid(self, s: str) -> bool:
        characters = {'[': ']', '{': '}', '(': ')'}

        stack = []

        for c in s:
            if c in characters.keys(): stack.append(c)
            else:
                if not len(stack) or characters[stack.pop()] != c: return False

        return not len(stack)