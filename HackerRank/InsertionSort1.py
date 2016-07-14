#!/bin/python
def insertionSort(ar):  
    e = ar[-1]
    position_to_insert = len(ar) - 1
    while position_to_insert >= 0:
        if position_to_insert == 0:
            ar[position_to_insert] = e
        elif ar[position_to_insert - 1] > e:
            ar[position_to_insert] = ar[position_to_insert - 1]
            print " ".join(map(str, ar))
        else:
            ar[position_to_insert] = e
            break
        position_to_insert = position_to_insert - 1
    print " ".join(map(str, ar))        
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)