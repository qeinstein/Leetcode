class Solution:
    def isValid(self, s:str)->bool:
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            elif char in ")}]":
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if char == ')' and top != '(':
                    return False
                elif char == '}' and top != '{':
                    return False
                elif char == ']' and top != '[':
                    return False
            else:
                return False
        if len(stack) != 0:
            return False
        return True