#Author: Madhu Chakravarthy
#Date: 21-05-2018
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype str
        """
        length = len(s)

        if length <= numRows`:
            return s
        zigZag = []

        for i in range(numRows):
            zigZag.append([])

        zigZag[0].append(s[0])

        curr = 1
        toggle =  True
        stringEmpty = False

        while curr < length:
            if toggle:
                for i in range(1, numRows):
                    if curr >= length:
                        stringEmpty = True
                        break
                    zigZag[i].append(s[curr])
                    curr += 1
                if stringEmpty:
                    break
                toggle = False
                continue
            else:
                for i in range(numRows-2, -1, -1):
                    if curr > length:
                        stringEmpty = True
                        break
                    zigZag[i].append(s[curr])
                    curr += 1
                if stringEmpty:
                    break
                toggle = True
        string = ""
        for row in zigZag:
            string += "".join(row)
        return string


if __name__ == "__main__":
    sol =  Solution()
    print sol.convert('PAYPALISHIRING', 3)
    print sol.convert('PAYPALISHIRING', 4)


