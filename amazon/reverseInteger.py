#Author: Madhu Chakravarthy
#Date: 09-02-2018
class Solution(object):
    def reverse(self,x):
        """
        type: x: int
        rtype: int
        """
        if x == 0:
            return 0
        newx = list(str(x))
        sign = 1
        if newx[0] == '-':
            sign = -1
            del newx[0]
        length = len(newx)
        for i in range(length/2):
            newx[i], newx[length - 1 - i] = newx[length -1 -i], newx[i]
        if newx[0] == '0':
            del newx[0]
        ret = int(''.join(newx))
        ret = sign * ret if ret <= 2**31-1 else 0
        return ret

if __name__ == "__main__":
    sol =  Solution()
    num = 120
    print sol.reverse(num)
    num = -1201
    print sol.reverse(num)
    num = -12011
    print sol.reverse(num)
    num = 2**31 
    print sol.reverse(num)
