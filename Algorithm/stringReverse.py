# Author: Madhu Chakravarthy
# Date: 24-04-2017

def stringReverse(string):

    length = len(string)
    revString = [""] * length

    for i in range(length/2 + 1):

        revString[i] = string[length -1 -i]
        revString[length -1 -i] = string[i]

    return "".join(revString)


print stringReverse("Test")
print stringReverse("Test")
print stringReverse("length")
print stringReverse("lenngth")


