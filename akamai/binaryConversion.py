#Author: Madhu Chakravarthy
#Date: 19-04-2018
def binaryConversion(number):

    binString = ""
    while number > 0:
        binString += str(number % 2)
        number = number // 2
    return binString[::-1]

if __name__ == "__main__":
    print binaryConversion(2)
    print binaryConversion(25)
    print binaryConversion(5)

