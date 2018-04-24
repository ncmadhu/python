#Author: Madhu Chakravarthy
#Date: 19-04-2018
import sys
def thirdMax(numbers):

    m1 = m2 = m3 = -sys.maxint - 1

    for num in numbers:
        if num > m1:
            m3 = m2
            m2 = m1
            m1 = num
        elif num > m2:
            m3 = m2
            m2 = num
        elif num > m3:
            m3 = num

    return m3

if __name__ == "__main__":
    print thirdMax([9, 1, 5, 0])
