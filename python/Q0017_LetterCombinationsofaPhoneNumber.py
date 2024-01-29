from typing import List

class Solution:
    def letterCombinations(self, n: str) -> List[str]:
        if len(n)==0:
            return []
        options = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        ans = ['']
        
        for digit in n:
            digit = int(digit)
            for _ in range(len(ans)):
                curr = ans.pop(0)
                for letter in options[digit]:
                    ans.append(curr + letter)
        return ans