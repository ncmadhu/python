#Author: Madhu Chakravarthy
#Date: 14-03-2018
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x

        start = 0
        end = x

        while start <= end:
            mid = (start + end) // 2

            if x == mid * mid:
                return mid
            elif mid * mid < x:
                start = mid + 1
                ans = mid
            else:
                end = mid - 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.mySqrt(4)
    print sol.mySqrt(8)
    print sol.mySqrt(9)
