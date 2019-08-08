# Author: Madhu Chakravarthy
# Date: 6-06-2017


def fibonacciNumbers(maxFibNumber):

    sum = 0
    a = 0
    b = 1
    while True:

        #print a
        a,b = b, a + b

        if not a % 2:
            sum += a

        if b > maxFibNumber:
            break
    #print a
    #print b
    print sum


"""
Every Third number is even in fibonacci
"""

def evenFibonacciSum(limit):

    sum = 0
    a = 1
    b = 1
    c = a + b

    while c < limit:

        sum += c
        a = b + c
        b = c + a
        c = a + b

    print sum


if __name__ == "__main__":

    fibonacciNumbers(4000000)
    evenFibonacciSum(4000000)





  
