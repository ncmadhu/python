#Author: Madhu Chakravarthy
#Date: 24-02-2018
class Solution(object):
    def longestPalindrome(self, string):
        """
        :type string: string
        :rtype string
        """
        length = len(string)
        start = 0
        end = 0
        for i in range(length):
            len1 = self.expandAroundCentre(string, i, i)
            len2 = self.expandAroundCentre(string, i, i+1)
            plen = max(len1, len2)
            if plen > end - start:
                start = i - (plen - 1) / 2
                end = i + plen / 2
        return string[start: end + 1]

    def expandAroundCentre(self, string, left, right):
        L = left
        R = right
        while L >=0 and R < len(string) and string[L] == string[R]:
            L -= 1
            R += 1
        return R - L - 1

if __name__ == "__main__":
    sol = Solution()
    string = 'banana'
    print sol.longestPalindrome(string)


