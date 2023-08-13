class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        negative = False
        if x < 0:
            x *= -1
            negative = True
        
        while x > 0:
            res *= 10
            res += x%10
            x = x//10
        if negative == True:
            res *= -1
        
        if res < -(2**31) or res > 2**31:
            return 0
        else:
            return res