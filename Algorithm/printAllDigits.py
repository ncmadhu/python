#!/bin/python
# Author: Madhu Chakravarthy
# Date: 1-1-2018

def printAllDigits(number):

    while number != 0:
        remainder = number % 10
        number = number / 10
        print remainder

if __name__ == "__main__":
    printAllDigits(1234)
