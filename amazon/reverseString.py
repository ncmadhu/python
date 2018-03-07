#Author: Madhu Chakravarthy
#Date: 28-02-2018
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        #calculate length of the string
        length =  len(s)

        strList = list(s)

        for i in range(length/2):
            strList[i], strList[length - 1 - i] = strList[length - 1 - i], strList[i]

        return "".join(strList)

if __name__ == "__main__":
    sol = Solution()
    s = "hello"
    print sol.reverseString(s)
