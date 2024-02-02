from typing import List

# Time Complexity: O(n) / Space Complexity: O(n)
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = '123456789'
        ans = []
        for length in range(len(str(low)), len(str(high))+1):
            for i in range(10-length):
                num = int(digits[i:i+length])
                if num >= low and num <= high:
                    ans.append(num)
        
        return ans