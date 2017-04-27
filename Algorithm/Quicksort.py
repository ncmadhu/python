# Author: Madhu Chakravarthy
# Date: 27-04-2017

counter = 0

def quicksort(array):

    global counter
    counter += 1
    length = len(array)

    if length == 1 or length == 0:

        return array

    pivot = array.pop(0)

    left =[]
    right = []

    for element in array:

        if element <= pivot:
            left.append(element)

        else:
            right.append(element)

    left = quicksort(left)
    right = quicksort(right)
    return left + [pivot] + right

if __name__ == "__main__":

    counter = 0
    print "[99,23,11,45,22,22]: {}".format(quicksort([99,23,11,45,22,22]))
    print "counter: {}".format(counter)
    counter = 0
    print "[22,22]: {}".format(quicksort([22,22]))
    print "counter: {}".format(counter)
    counter = 0
    print "[99,23,45,22,22]: {}".format(quicksort([99,23,45,22,22]))
    print "counter: {}".format(counter)
    counter = 0
    print "[99]: {}".format(quicksort([99]))
    counter = 0
    print "counter: {}".format(counter)
    counter = 0
    print "[]: {}".format(quicksort([]))
    print "counter: {}".format(counter)
    counter = 0
    print "[100,150,34,30,12,5,1,122,10,20,2,35,32,56,23,89,33,55,11,0]: {}".format(quicksort([100,150,34,30,12,5,1,122,10,20,2,35,32,56,23,89,33,55,11,0]))
    print "counter: {}".format(counter)
    counter = 0
    print quicksort([54,26,93,17,77,31,44,55,20])
    print "counter: {}".format(counter)
    counter = 0
    print quicksort([54,54,26,93,17,77,31,44,55,20])
    print "counter: {}".format(counter)

