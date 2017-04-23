# Author: Madhu Chakravarthy
# Date: 23-04-2017

def binaryConversion(number):

    binString = "" 

    while number > 0:
        binString += str(number % 2)
        number = number // 2

    return binString[::-1]


print binaryConversion(2)
print binaryConversion(3)
print binaryConversion(4)
print binaryConversion(5)
print binaryConversion(6)
