#Author: Madhu Chakravarthy
#Date: 08-02-2018
import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        random.shuffle(nums)
        self.quickSort(nums, 0, len(nums) - 1)
        return nums[-k]

    def quickSort(self, nums, low, high):
        if low < high:
            pivot = self.partition(nums, low, high)
            self.quickSort(nums, low, pivot - 1)
            self.quickSort(nums, pivot + 1, high)

    def partition(self, nums, low, high):
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        i += 1
        nums[i], nums[high] = nums[high], nums[i]
        return i

if __name__ == "__main__":
    sol = Solution()
    arr = [9,7,5,11,12,2,14,3,10,6]
    random.shuffle(arr)
    print arr
    print sol.findKthLargest(arr, 1)
    print sol.findKthLargest(arr, 2)
    print sol.findKthLargest(arr, 3)
    print sol.findKthLargest(arr, 4)
