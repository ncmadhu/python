# Author: Madhu Chakravarthy
# Date: 23-04-2017

def selectionSort(ulist):

    for fillSlot in range(len(ulist) -1, 0, -1):

        posMax = 0

        for location in range(1, fillSlot + 1):

            if ulist[location] > ulist[posMax]:

                posMax = location

        ulist[posMax], ulist[fillSlot] = ulist[fillSlot], ulist[posMax]

    return ulist

print selectionSort([5,8,2,1])
print selectionSort([5])
print selectionSort([])
print selectionSort([1,2,3,4])
print selectionSort([34,1,23,2,2])
