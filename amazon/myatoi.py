#-Author: Madhu Chakravarthy
#Date: 09-02-2018
class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if len(s) == 0:
            return 0
        ls = list(s)
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+']:
            del ls[0]
        ret = 0
        i = 0
        while i < len(ls) and ls[i].isdigit():
            ret = ret*10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * ret, 2**31-1))

if __name__ == "__main__":
    sol = Solution()
    s = '   -12345'
    print sol.myAtoi(s)
    s = '1'
    print sol.myAtoi(s)
