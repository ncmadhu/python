#!/bin/python
def insertionSort(ar): 
    
    for i in range(1,len(ar)):
        valueToInsert = ar[i]
        insertPosition = i
        while insertPosition > 0 and ar[insertPosition - 1] > valueToInsert:
            ar[insertPosition] = ar[insertPosition - 1]
            insertPosition = insertPosition -1
        ar[insertPosition] = valueToInsert
        print " ".join(map(str, ar))
    
    
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)