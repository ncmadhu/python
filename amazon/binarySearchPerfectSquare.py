#Author: Madhu Chakravarthy
#Date: 20-03-2018
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start = 0
        end = num
        while start <= end:
            mid = (start + end) / 2
            prod = mid * mid
            if prod == num:
                return True
            elif prod > num:
                end =  mid - 1
            else:
                start =  mid + 1

        return False

if __name__ == "__main__":
    sol = Solution()
    print sol.isPerfectSquare(16)
    print sol.isPerfectSquare(14)
    print sol.isPerfectSquare(1)
    print sol.isPerfectSquare(0)
    print sol.isPerfectSquare(-10)

