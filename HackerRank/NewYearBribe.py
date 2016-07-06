#!/bin/python

import sys

def calculate_bribe(queue):
    bribe = 0
    for i in range(len(q) - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            print "Too chaotic"
            return

        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribe += 1
    print bribe
    return
    

T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    q = map(int,raw_input().strip().split(' '))
    # your code goes here
    calculate_bribe(q)
              