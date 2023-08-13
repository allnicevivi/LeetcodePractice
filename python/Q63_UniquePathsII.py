from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[-1 for j in range(n)] for i in range(m)]

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        else:
            dp[0][0] = 1

        for i in range(1, n):
            if(obstacleGrid[0][i] == 0):
                dp[0][i] = dp[0][i-1]
            else:
                dp[0][i] = 0

        for i in range(1, m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    cnt = dp[i-1][j]
                    if j > 0:
                        cnt += dp[i][j-1]
                    dp[i][j] = cnt
                
        return dp[m-1][n-1]