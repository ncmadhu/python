#Author: Madhu Chakravarthy
#Date: 23-04-2018
class Solution(object):
    def firstUniqChar(self,s):
        """
        :type s: str
        :rtype: int
        """
        charMap = {}
        for char in s:
            charMap[char] = charMap.get(char, 0) + 1

        for i, char in enumerate(s):
            if charMap[char] == 1:
                return i

        return -1

if __name__ == "__main__":
    sol =  Solution()
    print sol.firstUniqChar('leetcode')
