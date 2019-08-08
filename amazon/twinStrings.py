#Author: Madhu Chakravarthy
#Date: 09-08-2018
def twins(stringA, stringB):
    if len(stringA) != len(stringB):
        return 'NO'

    if stringA == stringB:
        return "YES"

    swapEvenString = swapEven(stringB)

    if stringA == swapEvenString:
        return "YES"
    elif stringA == swapOdd(swapEvenString):
        return 'YES'
    elif stringA == swapOdd(stringB):
        return "YES"

    return "NO"
    


def swapEven(string):

    start = 0
    length = len(string)

    strList = list(string)

    while start+2 < length:
        strList[start], strList[start+2] = strList[start+2], strList[start]
        start += 4

    return "".join(strList)

def swapOdd(string):
    start = 1
    length = len(string)
    strList = list(string)
    while start+2 < length:
        strList[start], strList[start+2] = strList[start+2], strList[start]
        start += 4

    return "".join(strList)

if __name__ == "__main__":

    print swapEven('cbaad')
    print swapEven('cbad')
    print swapEven('cbadgfehh')
    print swapOdd('adcb')
    print swapOdd('abc')
    print swapOdd('adcbehgf')
    print swapEven(swapOdd('cdabghef'))
    print twins('abcd', 'cdab')
    print twins('dcba', 'abcd')



