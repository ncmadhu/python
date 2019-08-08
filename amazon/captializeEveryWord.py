#Author: Madhu Chakravarthy
#Date: 07-05-2018
class Solution(object):
    def capitalizeWord(self, sentence):
        diff = ord('a') - ord('A')
        newSentence = ''
        for char in sentence:
            asciiVal = ord(char)
            if ord('a') <= asciiVal <= ord('z'):
                newChar = chr(asciiVal - diff)
                newSentence += newChar
            else:
                newSentence += char
        return newSentence
        

if __name__ == "__main__":
    sol =  Solution()
    print sol.capitalizeWord("sample sentence is this")
