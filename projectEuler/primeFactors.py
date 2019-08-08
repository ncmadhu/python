# Author: Madhu Chakravarthy
# Date: 06-06-2017

import math

def primeFactors(n):

    factors = []

    while n % 2 == 0:
        factors.append(2)
        n = n / 2

    i = 3

    while i <= math.sqrt(n):

        while n % i == 0:
            factors.append(i)
            n = n / i

        i += 2


    if n > 2:
        factors.append(n)

    return factors


if __name__ == "__main__":

    print primeFactors(315)
    print primeFactors(600851475143)
