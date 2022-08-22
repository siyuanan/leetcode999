# queue and stack
class Solution:
    # 227. Basic Calculator II
    def calculate(self, s: str) -> int:
        if len(s) <= 0: 
            return 0

        stack = deque()
        operation = '-' if s[0] == '-' else '+'
        curNumber = 0

        for i in range(len(s)): 
            # print(f'i: {i}')
            # get the current number
            if s[i] >= '0' and s[i] <= '9': 
                curNumber = 10 * curNumber + int(s[i])

            # reach the next operation
            # finish previous operation
            if (s[i] in ['+', '-', '*', '/']) or (i == len(s)-1): 
                # print(f'si: {s[i]}')
                # print(curNumber)
                if operation == '+': 
                    stack.append(curNumber)
                elif operation == '-': 
                    stack.append(-curNumber)
                elif operation == '*': 
                    stack.append(stack.pop() * curNumber)
                else: 
                    stack.append(int(stack.pop() / curNumber))
                operation = s[i]
                curNumber = 0
                i += 1
                # print(stack)
                # print(operation)      

        res = 0
        while len(stack) > 0: 
            res += stack.pop()
        return res
