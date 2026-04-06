class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for val in tokens:
            if val == "+":
                first = stack.pop()
                second = stack.pop()
                ans = first + second
                stack.append(int(ans))
            elif val == "-":
                first = stack.pop()
                second = stack.pop()
                ans = second - first
                stack.append(int(ans))
            elif val == "*":
                first = stack.pop()
                second = stack.pop()
                ans = first * second
                stack.append(int(ans))
            elif val == "/":
                first = stack.pop()
                second = stack.pop()
                ans = second / first
                stack.append(int(ans))
            else:
                stack.append(int(val))

        return stack[-1]
        