class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_len = 0
        s_len = len(s)
        for i in range(s_len):
            l, r = i, i
            EvenNotvalid = False
            OddNotvalid = False
            while l >= 0 and r < s_len:
                if (r+1) < s_len and s[l] == s[r+1] and EvenNotvalid == False:
                    if ((r+1)-l+1) > max_len:
                        start = l
                        max_len = (r+1)-l+1
                else:
                    EvenNotvalid = True
                
                if s[l] == s[r] and OddNotvalid == False:
                    if (r-l+1) > max_len:
                        start = l
                        max_len = r-l+1
                else:
                    OddNotvalid = True
                
                if EvenNotvalid and OddNotvalid:
                    break
                l -= 1
                r += 1

        return s[start:start+max_len]

