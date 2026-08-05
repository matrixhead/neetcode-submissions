class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opentoclosing = {"(":")","{":"}","[":"]"}
        for c in s:
            if c in opentoclosing:
                stack.append(c)
            elif (len(stack)!=0) and opentoclosing[stack[-1]] == c:
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return  True
        return False
