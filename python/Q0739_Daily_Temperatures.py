
from typing import List

# Method 2 (Time Complexity: O(n), 80.09% / Space Complexity: O(n), 86.73%)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)
        stack = []

        for i in range(len(temperatures)-1, -1, -1):

            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            
            if stack:
                res[i] = stack[-1]-i

            stack.append(i)
        
        return res

# Method 1 (Time Complexity: O(72^2), 5.35% / Space Complexity: O(max(72, n)), 99.82%)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        day = [[] for _ in range(72)]
        res = [0]*len(temperatures)
        for curr_day, curr_temp in enumerate(temperatures):
            day[curr_temp-30].append(curr_day)
            for prev_temp, prev_days in enumerate(day[0:curr_temp-30]):
                if prev_days != []:
                    for prev_day in prev_days:
                        res[prev_day] = curr_day-prev_day
                    day[prev_temp] = []
        
        return res