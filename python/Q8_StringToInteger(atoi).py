class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        start = False
        negative = False
        sign = False
        for i in s:
            print(i)
            print(res, '\n')
            if start == False:
                if i.isalpha():
                    break
                if sign:
                    if i.isdigit() == False:
                        return 0
                else:
                    if i == '-':
                        negative = True
                        sign = True
                    elif i == '+':
                        sign = True
                        continue
                    elif i == ' ' :
                        continue
                    elif i == '.':
                        return 0

                if i.isdigit():
                    start = True
            if start:
                if i.isdigit() == False:
                    break
                else:
                    res *= 10
                    res += int(i)
        if negative:
            res *= -1
        if res < -2**31:
            return -2**31
        elif res > 2**31-1:
            return 2**31-1
        else:
            return res