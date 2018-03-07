#Author: Madhu Chakravarthy
#Date: 28-02-2018
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #calculate length of the string
        length = len(s)
        charMap = {}
        for i in range(length):
            if s[i] not in charMap:
                found = False
                for j in range(i+1, length):
                    if s[i] == s[j]:
                        found = True
                        break
                if not found:
                    return i
                else:
                    charMap[s[i]] = i
        return -1

    def firstUniqCharAnother(self, s):
        """
        :type s:str
        :rtype: int
        """
        index = -1
        charMap = {}
        for char in s:
            charMap[char] = charMap.get(char, 0) + 1

        for i, char in enumerate(s):
            if charMap[char] == 1:
                return i
        return index

if __name__ == "__main__":
    sol = Solution()
    s = 'leetcode'
    print sol.firstUniqChar(s)
    s = 'eetcode'
    print sol.firstUniqChar(s)
    s = 'eeed'
    print sol.firstUniqChar(s)
    s = 'eee'
    print sol.firstUniqChar(s)
    s = 'leetcode'
    print sol.firstUniqCharAnother(s)
    s = 'eetcode'
    print sol.firstUniqCharAnother(s)
    s = 'eeed'
    print sol.firstUniqCharAnother(s)
    s = 'eee'
    print sol.firstUniqCharAnother(s)
