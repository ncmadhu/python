# Author: Madhu Chakravarthy
# Date: 27-04-2017

counter = 0
def quicksort(arr, lo, hi):
    
    global counter
    counter += 1

    if lo < hi:

        p = partition(arr, lo, hi)
        quicksort(arr, lo, p)
        quicksort(arr, p + 1, hi)
    return arr


def partition(arr, lo, hi):

    pivot = arr[lo]
    print pivot

    i = lo
    j = hi

    while j > 0:

        while arr[i] < pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1

        print i,j

        if i >= j:
            arr[i],arr[j] = arr[j],arr[i]
            return j
        arr[i],arr[j] = arr[j],arr[i]


if __name__ == "__main__":

    counter = 0
    print "[99,23,11,45,22,22]: {}".format(quicksort([99,23,11,45,22,22], 0, 5))
    print "counter: {}".format(counter)
    """
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
    """
