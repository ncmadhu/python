#Author: Madhu Chakravarthy
#Date: 19-04-2018
import sys

def secondMax(numbers):
    m1 = m2 = -sys.maxint - 1
    for num in numbers:
        if num > m2:
            if num > m1:
                m1, m2 = num, m1
            else:
                m2 = num
    return m2

if __name__ == "__main__":
    print secondMax([5, 8, 3, 9])
