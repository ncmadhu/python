#Author: Madhu Chakravarthy
#Date: 15-03-2018
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pivot = self.findPivot(nums)
        if pivot == -1:
            return self.binarySearch(nums, target, 0, len(nums) - 1)

        if nums[pivot] == target:
            return pivot
        if nums[0] <= target:
            return self.binarySearch(nums, target, 0, pivot - 1)
        return self.binarySearch(nums, target, pivot + 1, len(nums) - 1)

    def findPivot(self, nums):

        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if mid < end and nums[mid] > nums[mid+1]:
                return mid
            if mid > start and nums[mid] < nums[mid-1]:
                return mid - 1
            if nums[start] > nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def binarySearch(self, nums, target, start, end):
        if start == end and nums[start] != target:
            return -1
        if start > end:
            return -1
        mid = (start + end) / 2

        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            return self.binarySearch(nums, target, start, mid-1)
        else:
            return self.binarySearch(nums, target, mid+1, end)

if __name__ == "__main__":
    sol = Solution()
    nums = [4,5,6,7,8,9,1,2,3]
    target =  3
    print sol.search(nums, target)
    nums = [1,2,3,4,5,6,7,8,9]
    target =  3
    print sol.search(nums, target)
    nums = [1,3]
    target =  0
    print sol.search(nums, target)
    nums = [3,5,1]
    target =  3
    print sol.search(nums, target)


            
