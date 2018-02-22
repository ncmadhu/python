#Author: Madhu Chakravarthy
#Date: 08-02-2018

class Solution(object):
    def quickSort(self, arr, low, high):
        if low < high:
            pivot = self.partition(arr, low, high)
            self.quickSort(arr, low, pivot - 1) # before pivot
            self.quickSort(arr, pivot + 1, high) # after pivot

    def partition(self, arr, low, high):
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1],arr[high] = arr[high], arr[i+1]
        return i + 1

if __name__ == "__main__":
    sol = Solution()
    arr = [9,7,5,11,12,2,14,3,10,6]
    sol.quickSort(arr, 0, len(arr) - 1)
    print arr
