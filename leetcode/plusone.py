# Author: Madhu Chakravarthy
# Date: 14-01-2018

class Solution(object):
    def plusone(self, digits):
        """
        :type digits: List[int]
        :rtype List[int]
        """
        length = len(digits)
        sum = 0
        for i,v in enumerate(digits):
            sum += 10 ** (length - 1 - i) * v
        sum = sum + 1
        retval = []
        while(sum):
            retval.insert(0,sum % 10)
            sum = sum / 10
        return retval

if __name__ == "__main__":
    solution = Solution()
    digits = [4,7,3]
    print solution.plusone(digits)
