#Author: Madhu Chakravarthy
#Date: 07-02-2018

class Solution(object):

    def longestPalindrome(self, s):
        subStrings = set(self.getSubStrings(s))
        reversedSubStrings = set(self.getSubStrings(self.stringReverse(s)))
        palindromeStrings = set.intersection(subStrings, reversedSubStrings)
        print palindromeStrings
        maxString = ""
        for string in palindromeStrings:
            if len(string) > len(maxString):
                maxString =  string
        return maxString

    def stringReverse(self, string):

        length = len(string)
        newString = [''] * length 

        for i in range(length/2):
            newString[i], newString[length - 1 - i] = string[length - 1 - i], string[i]
        return "".join(newString)


    def getSubStrings(self, string):
        characters = []
        length = len(string)
        start = 0
        current = 0
        subStrings = []
        while start < length and current < length:
            if string[current] not in characters:
                characters.append(string[current])
                current += 1
            else:
                del characters[0]
                subStrings.append(string[start:current])
                start += 1
        if start < current:
            subStrings.append(string[start:current])

        return subStrings

if __name__ == "__main__":
    sol = Solution()
    string = "abacdfgdcabba"
    print sol.longestPalindrome(string)
    string = "adcccdcfghhgf"
    print sol.longestPalindrome(string)
