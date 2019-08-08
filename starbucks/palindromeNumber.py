#Author: Madhu Chakravarthy
#Date: 21-05-2018
class Solution(object):
    def isPalindrome(self, x):
        """
        type x: int
        rtype: bool
        """
        newNum = 0
        num = x
        while num > 0:
            newNum  = (newNum * 10 ) + num % 10
            num = num / 10
        return True if newNum == x else False


if __name__ == "__main__":
    sol =  Solution()
    print sol.isPalindrome(121)
    print sol.isPalindrome(-121)
    print sol.isPalindrome(1221)
           
