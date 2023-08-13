class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            skip = numRows + (numRows - 2)
            res = ''
            if len(s)%skip == 0:
                head = len(s)//skip
            else:
                head = (len(s)//skip) + 1

            for i in range(numRows):
                if i == 0 or i == (numRows-1):
                    for j in range(head):
                        if skip*j + i < len(s):
                            res += s[skip*j + i]
                else:
                    for j in range(head):
                        if skip*j + i < len(s):
                            res += s[skip*j + i]
                        if skip*j + i + skip-2*i < len(s):
                            res += s[skip*j + i + skip-2*i]

        return res