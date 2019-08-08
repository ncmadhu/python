#Author: Madhu Chakravarthy
#Date: 24-04-2018
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        length = len(s)
        left = 0
        right = length - 1
        while left < right:
            leftChar = s[left]
            asciiValue  = ord(leftChar)
            if not (65 <= asciiValue <= 90 or 97 <= asciiValue <= 122 or 48 <= asciiValue <= 57):
                left += 1
                continue
            rightChar = s[right]
            asciiValue  = ord(rightChar)
            if not (65 <= asciiValue <= 90 or 97 <= asciiValue <= 122 or 48 <= asciiValue <= 57):
                right -= 1
                continue
            if leftChar.lower() != rightChar.lower():
                return False
            left += 1
            right -= 1

        return True
       

if __name__ == "__main__":
    sol =  Solution()
    print sol.isPalindrome("A man, a plan, a canal: Panama")
    print sol.isPalindrome("race a car")
    print sol.isPalindrome("0P")
    
