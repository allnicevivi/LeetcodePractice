from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for i in range(len(strs[0])):
            s_i = strs[0][i]
            for j in range(1, len(strs)):
                if (len(strs[j]) <= i) or (strs[j][i] != s_i):
                    return prefix
            prefix = prefix + s_i
        return prefix