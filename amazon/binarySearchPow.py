#Author: Madhu Chakravarthy
#Date: 22-03-2018
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if  n < 0:
            x =  1/x
            n = -n

        return self.calcPow(x,n)

    def calcPow(self, x, n):
        if n == 0:
            return 1
        half =  self.calcPow(x, n/2)
        if n % 2 == 0:
            return half * half
        else:
            return x * half * half

    def myPow2(self, x, n):

        if n == 0:
            return 1
        if n < 0:
            x =  1/x
            n = -n
        ans = 1
        while n > 0:
            if n % 2:
                ans = ans * x
            x =  x * x
            n = n/2
        return ans


if __name__ == "__main__":
    sol = Solution()
    print sol.myPow(2.00000, 10)
    print sol.myPow(2.10000, 3)
    print sol.myPow2(2.00000, 10)
    print sol.myPow2(2.10000, 3)
