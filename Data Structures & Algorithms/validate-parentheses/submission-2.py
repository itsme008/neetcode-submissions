class Solution:
    def isValid(self, s: str) -> bool:
        
        closed_brackets = {"}":"{", ")":"(", "]":"["}

        stack = []

        for i in s:
            if i in closed_brackets:
                if stack and stack[-1] == closed_brackets[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if not stack else False
