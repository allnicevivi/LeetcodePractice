class Solution:
    def intToRoman(self, num: int) -> str:
        sym_dict = {1:'I', 4:'IV', 5:'V', 9:'IX', 
                    10:'X', 40:'XL', 50:'L', 90:'XC', 
                    100:'C', 400:'CD', 500:'D', 900:'CM', 
                    1000:'M'}
        ans = ''
        x = 1000
        while num > 0:
            if num >= x:
                i = int(num // x)
                if i == 4 or i == 5 or i ==9:
                    ans += sym_dict[i*x]
                elif i <= 5:
                    ans += sym_dict[x]*i
                else:
                    ans += (sym_dict[5*x] + sym_dict[x]*(i-5))
                num -= i*x
            x *= 0.1    
            
        return ans