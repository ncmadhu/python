#!/bin/python
import sys
n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
num_swaps = 0
for i in range(n):
    swap_done =  False
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
            num_swaps += 1
            swap_done = True
    if not swap_done:
        break
print "Array is sorted in " + str(num_swaps) + " swaps."
print "First Element: " + str(a[0])
print "Last Element: " + str(a[-1])