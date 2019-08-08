# Author: Madhu Chakravarthy
# Date: 22-04-2017

def binarySearch(arr, left, right, element):

    if right >= left:

        mid = left + (right - left) / 2

        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            return binarySearch(arr, mid + 1, right, element)
        else:
            return binarySearch(arr, left, mid -1, element)
    else:

        return -1


print binarySearch([1,2,3,4,5], 0, 4, 1)
print binarySearch([1,2,3,4,5], 0, 4, 2)
print binarySearch([1,2,3,4,5], 0, 4, 3)
print binarySearch([1,2,3,4,5], 0, 4, 4)
print binarySearch([1,2,3,4,5], 0, 4, 5)
print binarySearch([5,9,10,12,14], 0, 4, 12)
print binarySearch([5,9,10,12,14], 0, 4, 1)



