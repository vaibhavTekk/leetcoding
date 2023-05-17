class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "*+/-":
                stack.append(int(i))
            else:
                if i == "+":
                    a = stack.pop()
                    stack[-1] = stack[-1] + a
                elif i == "*":
                    a = stack.pop()
                    stack[-1] = stack[-1] * a
                elif i == "/":
                    a = stack.pop()
                    stack[-1] = int(stack[-1] / a)
                elif i == "-":
                    a = stack.pop()
                    stack[-1] = stack[-1] - a
        return stack[0]