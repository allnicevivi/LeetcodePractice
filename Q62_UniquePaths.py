### Method 1 =====================================
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1 for _ in range(n)]

        for i in range(m-1):
            cnt = 1
            
            for j in range(1, n):
                row[j] += cnt
                cnt = row[j]
        return row[-1]

### Method 2 =====================================
import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def combination(x, y):
            return math.factorial(x+y)/(math.factorial(x)*math.factorial(y))

        
        return int(combination(n-1, m-1))