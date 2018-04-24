#Author: Madhu Chakravarthy
#Date: 23-04-2018
class Solution(object):
    def reverseString(self, s):
        length = len(s)
        sList = list(s)
        for i in range(length/2):
            sList[i], sList[length - 1 -i] = sList[length -1 -i], sList[i]

        return "".join(sList)

if __name__ == "__main__":
    sol =  Solution()
    print sol.reverseString("hello")
    print sol.reverseString("helo")
