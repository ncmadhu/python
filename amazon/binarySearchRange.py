#Author: Madhu Chakravarthy
#Date: 16-03-2018
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        left_end = self.findExtremeIndex(nums, target, True)

        if left_end == len(nums) or nums[left_end] != target:
            return [-1,-1]

        right_end = self.findExtremeIndex(nums, target, False)
        return [left_end, right_end -1]

    def findExtremeIndex(self, nums, target, left):
        start = 0
        end = len(nums)

        while start < end:
            mid = (start + end) / 2
            if nums[mid] > target or (left and nums[mid] == target):
                end = mid
            else:
                start = mid + 1
        return start

if __name__ == "__main__":
    sol = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    print sol.searchRange(nums,8)
    nums = [1,2,5,7,8,8,8,10]
    print sol.searchRange(nums,8)
    nums = []
    print sol.searchRange(nums,8)
    nums = [8]
    print sol.searchRange(nums,8)
    nums = [1]
    print sol.searchRange(nums,8)
