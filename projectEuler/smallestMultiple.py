# Author: Madhu Chakravarthy
# Date: 08-06-2017

from functools import reduce

def smallestMultiple(maxnumber):

    numbers = range(1, maxnumber + 1)

    return reduce(lcm, numbers)


def lcm(a,b):

    return a * b / gcd(a,b)

def gcd(a,b):

    if a % b == 0:
        return b

    return gcd(b, a % b)




if __name__ == "__main__":

    print gcd(48,18)
    print lcm(2,3)

    print smallestMultiple(10)
    print smallestMultiple(20)

