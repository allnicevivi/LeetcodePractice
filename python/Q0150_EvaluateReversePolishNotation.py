from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        exp = ['+', '-', '*', '/']
        stack = []
        for s in tokens:
            if s in exp:
                if s == '+':
                    stack[-2] += stack[-1]
                elif s == '-':
                    stack[-2] -= stack[-1]
                elif s == '*':
                    stack[-2] *= stack[-1]
                elif s == '/':
                    stack[-2] = int(stack[-2]/stack[-1])
                stack.pop()
            else:
                stack.append(int(s))
        
        return stack[0]


