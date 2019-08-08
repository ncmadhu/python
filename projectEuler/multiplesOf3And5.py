# Author: Madhu Chakravarthy
# Date: 6-05-2017


def sumOfMultiplesOf3And5(n):

    sum = 0

    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i


    return sum


def sumDivisibleBy(n, maxNumber):

    target = maxNumber - 1
    p = target / n

    return n * (p * (p + 1)) / 2



if __name__ == "__main__":

    print sumOfMultiplesOf3And5(10)
    print sumOfMultiplesOf3And5(100)
    print sumOfMultiplesOf3And5(1000)

    print sumDivisibleBy(3, 1000) + sumDivisibleBy(5, 1000) - sumDivisibleBy(15, 1000)

