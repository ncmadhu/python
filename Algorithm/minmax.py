#!/bin/python
# Author: Madhu Chakravarthy
# Date: 21-12-2017

import sys

def calculateMinMax(numList):
    listSum = reduce(lambda x,y: x+y, arr)
    min = listSum - arr[0]
    max = listSum - arr[0]
    for i in range(1, len(arr)):
        newSum = listSum - arr[i]
        if newSum < min:
            min = newSum
        if newSum > max:
            max = newSum
    return min, max

if __name__ == "__main__":
    arr = map(int, raw_input().strip().split(' '))
    min, max = calculateMinMax(arr)
    print "{0} {1}".format(min, max)
