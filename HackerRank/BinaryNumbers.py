#!/bin/python

import sys


n = int(raw_input().strip())
binstring = ''
consecutive_one = 0
num_one = 0
while n > 0:
    rem = n % 2
    if rem:
        num_one += 1
    else:
        #print n,binstring,num_one
        if num_one > consecutive_one:
            consecutive_one = num_one
        num_one = 0
    #print n,binstring,num_one
    binstring += str(rem)
    n = n / 2
    #print n
    #print binstring
    
#print binstring[::-1]
if num_one > consecutive_one:
    consecutive_one = num_one
print consecutive_one
