#Author: Madhu Chakravarthy
#Date: 23-04-2018
class Solution(object):
    def reverse(self,x):
        num = str(x)
        sign = 1
        if num[0] == '-':
            sign = -1
            num = num[1:]
        reverseNum = 0
        length = len(num)
        for index in range(length -1 , -1, -1):
            reverseNum = reverseNum * 10 + int(num[index])

        reverseNum = sign *  reverseNum if reverseNum <= 2**31 - 1 else 0

        return reverseNum

if __name__ == "__main__":
    sol =  Solution()
    print sol.reverse(123)
    print sol.reverse(-123)
    print sol.reverse(-120)
    print sol.reverse(1534236469)

