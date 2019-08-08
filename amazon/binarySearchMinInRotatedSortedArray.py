#Author: Madhu Chakravarthy
#Date: 16-03-2018
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        start =  0
        end = len(nums) - 1
        pivot =  self.findPivot(nums, start, end)
        if pivot == -1:
            return nums[0]
        else:
            return nums[pivot+1]

    def findPivot(self, nums, start, end):
        if start > end:
            return -1
        mid = (start + end) / 2
        if mid < end and nums[mid] > nums[mid+1]:
            return mid
        if mid > start and nums[mid-1] > nums[mid]:
            return mid - 1
        if nums[start] > nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
        return self.findPivot(nums, start, end)

if __name__ == "__main__":
    sol = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    print sol.findMin(nums)
