class Solution:
    def romanToInt(self, s: str) -> int:
        sym_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        val_now = 0
        val_last = 0
        for i in range(len(s)):
            val_now = sym_dict[s[len(s)-1-i]]
            if val_now < val_last:
                ans -= val_now
            else:
                ans += val_now
            val_last = val_now
        return ans
