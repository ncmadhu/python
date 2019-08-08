#Author: Madhu Chakravarthy
#Date: 17-03-2018
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if x <= arr[0]:
            return arr[:k]
        elif arr[-1] <= x:
            return arr[-k:]
        else:
            index =  self.binarySearch(arr, x)
            size = len(arr)
            low = max(0, index - k - 1)
            high = min(index + k - 1, size - 1)
            while high - low > k - 1:
                if low < 0  or (x - arr[low]) <= (arr[high] - x):
                    high -= 1
                elif high > size - 1 or (x - arr[low]) > (arr[high] - x):
                    low += 1
                else:
                    print "Unhandled"
                    print high
                    print low
                    break
            return arr[low:high+1]

    def binarySearch(self, arr, x):
        if not arr:
            return -1

        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = (start + end) / 2
            if arr[mid] ==  x:
                return mid
            elif arr[mid] < x:
                start = mid + 1
            else:
                end = mid - 1

        return start

if __name__ == "__main__":
    sol = Solution()
    """
    arr =  [1,4,5,6,8,9]
    print sol.findClosestElements(arr, 4, 7)
    arr =  [1,4,5,6,7,8]
    print sol.findClosestElements(arr, 4, 9)
    arr =  [1,4,5,6,7,8]
    print sol.findClosestElements(arr, 4, 5)
    """
    arr = [0,0,1,2,3,3,4,7,7,8]
    print sol.findClosestElements(arr, 3, 5)



