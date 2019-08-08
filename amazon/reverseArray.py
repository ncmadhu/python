#Author: Madhu Chakravarthy
#Date: 07-02-2018
class Solution(object):
    def reverseArray(self,arr):
        length = len(arr)
        for i in range(length/2):
            arr[i],arr[length-1-i] = arr[length-1-i],arr[i]

        return arr

if __name__ == "__main__":
    sol = Solution()
    arr = [1,2,3,4]
    print sol.reverseArray(arr)
    arr = [1,2,3,4,5]
    print sol.reverseArray(arr)
