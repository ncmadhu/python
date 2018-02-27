# Author: Madhu Chakravarthy
# Date: 09-08-2017

def mergeSort(unsortedList):

    length = len(unsortedList)
    if length == 1:
        return unsortedList
    l1 = unsortedList[0:length/2]
    l2 = unsortedList[length/2:]
    l1 = mergeSort(l1)
    l2 = mergeSort(l2)

    return merge(l1,l2)

def merge(l1,l2):

    newList = []

    while l1 and l2:

        if l1[0] > l2[0]:
            newList.append(l2[0])
            l2.pop(0)
        else:
            newList.append(l1[0])
            l1.pop(0)

    if l1:
        newList.extend(l1)

    if l2:
        newList.extend(l2)

    return newList

if __name__ == "__main__":

    print mergeSort([14,33,27,10,35,19,42,44])


