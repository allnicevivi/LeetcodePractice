class Solution:
    def isValid(self, s: str) -> bool:
        curve_dict = {')': '(', ']': '[', '}': '{'}
        left = []
        for i in s:
            if i in curve_dict.values():
                left.append(i)
            elif i in curve_dict.keys():
                if (len(left) == 0) or (curve_dict[i] != left[-1]):
                    return False
                else:
                    left.pop()
        if len(left) >= 1:
            return False
        else:
            return True