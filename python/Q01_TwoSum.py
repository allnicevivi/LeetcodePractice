from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 0
        dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict.keys():
                j = dict[diff]
                break
            else:
                dict[nums[i]] = i
                
        return ([i, j])

