#Author: Madhu Chakravarthy
#Date: 15-05-2018
def swap_case(s):
    stringList = list(s)
    for i, char in enumerate(stringList):
        asciiVal = ord(char)
        if ord('a') <= asciiVal <= ord('z'):
            stringList[i] = chr(asciiVal - 32) 
        elif ord('A') <= asciiVal <= ord('Z'):
            stringList[i] = chr(asciiVal + 32)
    return "".join(stringList)

if __name__ == "__main__":
    inputString = "Www.HackerRank.com"
    result = swap_case(inputString)
    print "%s --> %s" % (inputString, result)
