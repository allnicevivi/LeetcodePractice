from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        current = 0
        ans = 0
        while r-l > 0:
            area = min(height[l], height[r]) * (r-l)
            if area > ans:
                ans = area
            if height[l] <= height[r]:
                current = height[l]
                l += 1
                while r > l and height[l] < current:
                    l += 1
            else:
                current = height[r]
                r -= 1
                while r > l and height[r] < current:
                    r -= 1
        return ans