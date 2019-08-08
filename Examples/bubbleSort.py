# Author: Madhu Chakravarthy
# Date: 09-01-2018

def bubbleSort(unSortedlist):

    length = len(unSortedlist)
    for i in range(length - 1):
        swapped =  False
        for j in range(length - 1):
            print j, j+1 
            if unSortedlist[j] > unSortedlist[j+1]:
                unSortedlist[j],unSortedlist[j+1] = unSortedlist[j+1],unSortedlist[j]
                swapped = True
        if not swapped:
            break
    return unSortedlist

if __name__ == "__main__":
    print bubbleSort([14,33,27,35,10])

