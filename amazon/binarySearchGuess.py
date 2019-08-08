#Author: Madhu Chakravarthy
#Date: 14-03-2018
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start =  1
        end = n

        while start <= end:
            mid = (start + end) / 2
            result = self.guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                start = mid + 1
            else:
                end = mid - 1


    def guess(self, pick):
        myPick = 6
        if pick == myPick:
            return 0
        elif pick < myPick:
            return -1
        else:
            return 1

if __name__ == "__main__":
    sol = Solution()
    print sol.guessNumber(10)
