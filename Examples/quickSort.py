# Author: Madhu Chakravarthy
# Date: 10-01-2018

def quicksort(arr, left, right):
    i = left
    j = right
    print arr
    print left, right
    pivot = arr[(left + right - 0) / 2]
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        print i,j
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    if left < j:
        quicksort(arr, left, j)
    if i < right:
        quicksort(arr, i, right)

if __name__ == "__main__":

    arr = [10,80,30,90,40,50,70]
    quicksort(arr, 0, len(arr) - 1)
    print arr

