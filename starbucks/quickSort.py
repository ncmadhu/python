#Author: Madhu Chakravarthy
#Date: 21-05-2018
class Solution(object):
    def quickSort(self, arr):
        arrLength = len(arr)
        self.quickSortHelper(arr, 0, arrLength - 1)


    def quickSortHelper(self, arr, low, high):

        if low < high:
            partition = self.partition(arr, low, high)
            self.quickSortHelper(arr, low, partition - 1)
            self.quickSortHelper(arr, partition + 1, high)


    def partition(self, arr, low, high):

        pivot = arr[high]
        i = low - 1
        j = low

        while j < high:
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            j += 1

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1

if __name__ == "__main__":
    sol =  Solution()
    arr = [5, 2, 4, 10, 21, 45, 3, 4]
    print arr
    sol.quickSort(arr)
    print arr
