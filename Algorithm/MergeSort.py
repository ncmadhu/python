# Author: Madhu Chakravarthy
# Date: 26-04-2017

def mergeSort(unsortedList):

    length = len(unsortedList)

    if length == 1 or length == 0:
        return unsortedList

    middle = length / 2

    ul1 = unsortedList[0:middle]
    ul2 = unsortedList[middle:]

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

    print "[99,23,11,45,22,22]: {}".format(mergeSort([99,23,11,45,22,22]))
    print "[22,22]: {}".format(mergeSort([22,22]))
    print "[99,23,45,22,22]: {}".format(mergeSort([99,23,45,22,22]))
    print "[99]: {}".format(mergeSort([99]))
    print "[]: {}".format(mergeSort([]))

