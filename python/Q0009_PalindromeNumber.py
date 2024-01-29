class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        ans = True
        for i in range(len(x)//2):
            if x[i] != x[len(x)-1-i]:
                ans = False
                break
        return ans