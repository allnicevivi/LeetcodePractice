from typing import List

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        full = 0
        # diff_ls = []
        min_x = 0
        for i in range(len(capacity)):
            diff = capacity[i]-rocks[i]
            rocks[i] = diff
        rocks.sort()        
        for s in range(len(rocks)):
            min_x = rocks[s]
            if additionalRocks >= min_x:
                additionalRocks = additionalRocks - min_x
                full += 1
            else:
                break
        return full