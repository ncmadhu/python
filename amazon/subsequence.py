# Author: Madhu Chakravarthy
# Date: 07-02-2018
class Solution(object):
    def longestSubString1(self, string):
        length = len(string)
        maxSubStringLength = 0
        for i in range(length):
            for j in range(i+1, length + 1):
                if self.allUnique(string, i, j):
                    maxSubStringLength = max(maxSubStringLength, j - i)
        return maxSubStringLength

    def allUnique(self, string, start, end):
        characters = []
        for i in range(start, end):
            if string[i] in characters:
                return False
            characters.append(string[i])
        return True

    def longestSubString2(self, string):
        characters = []
        length = len(string)
        maxSubStringLength = 0
        start = 0
        current = 0
        while start < length and current < length:
            if string[current] not in characters:
                characters.append(string[current])
                current += 1
                maxSubStringLength = max(maxSubStringLength, current - start)
            else:
                del characters[0]
                start += 1
        return maxSubStringLength

    def longestSubString(self, string):
        charDict = {}
        length =  len(string)
        start = 0
        maxSubStringLength = 0
        for current in range(length):
            if string[current] in charDict:
                start =  max(charDict[string[current]], start)
            maxSubStringLength = max(maxSubStringLength, current - start + 1)
            charDict[string[current]] = current + 1
        return maxSubStringLength



if __name__ == "__main__":
    string = 'abcabbcdef'
    sol = Solution()
    print sol.longestSubString(string)
    string = 'aabbccdefghijkl'
    print sol.longestSubString(string)
            
