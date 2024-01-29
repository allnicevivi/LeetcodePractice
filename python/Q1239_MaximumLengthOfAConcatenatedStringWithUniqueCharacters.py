from typing import List

# Method 2 (Runtime: 99.18%/ Memory: 38.53%)
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        dp = [0]
        res = 0
        for s in arr:
            dup, sBit = 0, 0
            for c in s:
                dup |= sBit & (1 << (ord(c)-ord('a')))
                sBit |= 1 << (ord(c)-ord('a'))
            
            if dup > 0:
                continue
            
            for i in range(len(dp)-1, -1, -1):
                if (dp[i] & sBit) > 0:
                    continue
                dp.append(dp[i] | sBit)
                res = max(res, dp[-1].bit_count())

        return res
    
# Method 1 (Runtime: 20.83%/ Memory: 95.83%)
class Solution:
    def isUnique(self, s):
        char_set = set()
        for c in s:
            if c in char_set:
                return False
            char_set.add(c)
        
        return True
    
    def dfs(self, path, idx):

        if self.isUnique(path):
            self.maxLengthStr = max(self.maxLengthStr, len(path))
        elif (not self.isUnique(path)) or (idx == len(self.arr)-1):
            return 
        
        for i in range(idx, len(self.arr)):
            self.dfs(path+self.arr[i], i)

    def maxLength(self, arr: List[str]) -> int:
        
        self.maxLengthStr = 0
        self.arr = arr

        self.dfs('', 0)
        return self.maxLengthStr