class Solution(object):
    def numMusicPlaylists(self, n, goal, k):
        """
        :type n: int
        :type goal: int
        :type k: int
        :rtype: int
        """

        def factorial(x): 
            return 1 if (x==1 or x==0) else x * factorial(x - 1);  

        def part2(m):
            multi = 1
            for i in range(k):
                multi *= m-i
            multi *= (m-k)**(goal-k)
            return multi
        
        ans = 0
        for j in range(n):
            ans += (factorial(n)/(factorial(j)*factorial(n-j)))*part2(n-j)*(-1)**j
        ans = ans % (10**9 + 7)
        return ans