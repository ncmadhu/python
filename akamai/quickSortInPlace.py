#Author: Madhu Chakravarthy
#Date: 19-04-2018
def quickSort(unsortedList):

    length = len(unsortedList)

    if length <= 1:
        return unsortedList

    quickSortHelper(unsortedList, 0, length-1)

def quickSortHelper(arr, low, high):

    if low < high:
        p = partition(arr, low, high)
        quickSortHelper(arr, low, p - 1)
        quickSortHelper(arr, p + 1, high)

def partition(arr, low, high):

    pivot = arr[high]
    i = low - 1
    j = low

    while j <= high - 1:
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

if __name__ == "__main__":
    arr = []
    quickSort(arr)
    print arr
    arr = [1]
    quickSort(arr)
    print arr
    arr = [100,150,34,30,12,5,30,1,122,10,20,2,35,32,56,23,89,33,55,11,0]
    quickSort(arr)
    print arr

