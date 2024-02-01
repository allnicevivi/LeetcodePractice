from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        nums.sort()
        res = []
        for i in range(0, len(nums), 3):
            tmp = nums[i:i+3]
            if (tmp[1]-tmp[0] > k) or (tmp[2]-tmp[1] > k) or (tmp[2]-tmp[0] > k):
                return []
            res.append(tmp)
        
        return res