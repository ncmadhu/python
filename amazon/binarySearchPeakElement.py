#Author: Madhu Chakravarthy
#Date: 16-03-2018
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1

        def findPeakBinary(nums, start, end):
            if start == end:
                return start
            mid = (start + end) / 2
            if nums[mid] > nums[mid + 1]:
                return findPeakBinary(nums,start, mid)
            return findPeakBinary(nums, mid+1, end)

        return findPeakBinary(nums, start, end)

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1]
    print sol.findPeakElement(nums)
    nums = [1, 2, 3, 4, 2, 1]
    print sol.findPeakElement(nums)
    nums = [1, 2, 3, 4]
    print sol.findPeakElement(nums)
    nums = [4,3,2,1]
    print sol.findPeakElement(nums)
    nums = []
    print sol.findPeakElement(nums)
    nums = [1]
    print sol.findPeakElement(nums)
