# Author: Madhu Chakravarthy
# Date: 07-06-2017
import math


def palindromeProduct(digits):


    maxnumber = int(math.pow(10, digits) - 1)
    minnumber = int(math.pow(10, digits -1))
    #print maxnumber,minnumber
    palindromeNumber = None

    for i in range(maxnumber, minnumber - 1, -1):
        j = i
        while j >= minnumber:
            product = i * j
            if findPalindrome(product):
                #print "{} * {} = {}".format(i,j,product)
                if product > palindromeNumber:
                    palindromeNumber = product
            j = j - 1

    if palindromeNumber:
        print palindromeNumber


def findPalindrome(product):

    string = str(product)
    length = len(string)
    palindrome = True

    for i in range(length/2):

        if string[i] != string[length - 1 - i]:
            palindrome = False
            break
    return palindrome

if __name__ == "__main__":

    palindromeProduct(2)
    palindromeProduct(3)
