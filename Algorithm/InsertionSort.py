# Author: Madhu Chakravarthy
# Date: 23-04-2017

def insertionSort(ulist):

    for i in range(1, len(ulist)):

        value = ulist[i]
        hole = i

        while hole > 0 and ulist[hole -1] > value:

            ulist[hole] = ulist[hole - 1]
            hole = hole - 1

        ulist[hole] = value

    return ulist

print insertionSort([5,8,2,1])
print insertionSort([5])
print insertionSort([])
print insertionSort([1,2,3,4])
print insertionSort([34,1,23,2,2])
