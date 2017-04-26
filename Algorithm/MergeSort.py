# Author: Madhu Chakravarthy
# Date: 26-04-2017


def mergeSort(unsortedList):
    global counter
    counter += 1

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

    counter = 0
    print "[99,23,11,45,22,22]: {}".format(mergeSort([99,23,11,45,22,22]))
    print "counter: {}".format(counter)
    counter = 0
    print "[22,22]: {}".format(mergeSort([22,22]))
    print "counter: {}".format(counter)
    counter = 0
    print "[99,23,45,22,22]: {}".format(mergeSort([99,23,45,22,22]))
    print "counter: {}".format(counter)
    counter = 0
    print "[99]: {}".format(mergeSort([99]))
    counter = 0
    print "counter: {}".format(counter)
    counter = 0
    print "[]: {}".format(mergeSort([]))
    print "counter: {}".format(counter)
    counter = 0
    print "[100,150,34,30,12,5,1,122,10,20,2,35,32,56,23,89,33,55,11,0]: {}".format(mergeSort([100,150,34,30,12,5,1,122,10,20,2,35,32,56,23,89,33,55,11,0]))
    print "counter: {}".format(counter)

