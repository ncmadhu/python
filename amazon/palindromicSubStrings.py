#Author: Madhu Chakravarthy
#Date: 24-02-2018

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        count = 0
        for center in xrange(2*length):
            left = center / 2
            right = left + center % 2
            while left >=0  and right < length and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count

if __name__ == "__main__":
    sol =  Solution()
    string = "aaa"
    print sol.countSubstrings(string)

