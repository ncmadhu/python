# Author: Madhu Chakravarthy
# Date: 29-05-2017

def mergeTwoLists(l1, l2):

    l1 = mergeSort(l1)
    l2 = mergeSort(l2)
    return merge(l1,l2)

def mergeSort(unOrderedList):

    length = len(unOrderedList)

    if length == 1 or length == 0:
        return unOrderedList

    middle = length / 2

    ul1 = unOrderedList[0:middle]
    ul2 = unOrderedList[middle:]

    l1 = mergeSort(ul1)
    l2 = mergeSort(ul2)
    return merge(l1,l2)


def merge(l1,l2):

    c = []

    while l1 and l2:

        if l1[0] > l2[0]:
            c.append(l2[0])
            l2.pop(0)
        else:
            c.append(l1[0])
            l1.pop(0)

    while l1:

        c.extend(l1)
        l1 = []

    while l2:

        c.extend(l2)
        l2 = []

    return c



if __name__ == "__main__":

    l1 = [2,4,3,1]
    l2 = [5,8,7,6]

    print mergeTwoLists(l1,l2)

