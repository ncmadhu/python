#!/bin/python
# Author : Madhu Chakravarthy
# Date: 21-12-2017

import sys

def birthdayCakeCandles(n ,ar):
    max = ar[0]
    n_count = {}
    n_count[ar[0]] = 1
    for i in range(1, n):
        n_count[ar[i]] = n_count.get(ar[i], 0) + 1
        if ar[i] > max:
            max = ar[i]
    return n_count[max]

if __name__ == "__main__":
    n = int(raw_input().strip())
    ar = map(int, raw_input().strip().split(' '))
    result = birthdayCakeCandles(n, ar)
    print result

