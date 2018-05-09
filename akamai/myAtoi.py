#Author: Madhu Chakravarthy
#Date: 24-04-2018
class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        sign = 1
        stringList = list(s)
        length = len(stringList)
        if length == 0:
            return 0
        if stringList[0] in ['-', '+']:
            if stringList[0] == '-':
                sign = -1
            stringList.pop(0)

        num = 0
        i = 0

        while i < len(stringList) and stringList[i].isdigit():
            num = num * 10 + ord(stringList[i]) - ord('0')
            i += 1

        num = num * sign
        return max(-2**31,min(num, 2**31-1))

if __name__ == "__main__":
    sol =  Solution()
    print sol.myAtoi("42")
    print sol.myAtoi("   -42")
    print sol.myAtoi("4193 with words")
    print sol.myAtoi("words and 987")
    print sol.myAtoi("-91283472332")
    print sol.myAtoi("")
    print sol.myAtoi("+1")






