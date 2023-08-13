class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r, l = 0, 0
        char_dict = set()
        max_len = 0
        while r < len(s):
            if (s[r] not in char_dict) or r == 0:
                char_dict.add(s[r])
                r += 1
                max_len = max(max_len, r-l)
            else:
                char_dict.remove(s[l])
                l += 1
            print(s[l:r])
            
        return max_len