#Author: Madhu Chakravarthy
#Date: 14-03-2018
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def searchHelper(nums, target, start, end):
            if start == end and nums[start] != target:
                return -1
            mid = (start + end) / 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return searchHelper(nums, target, start, mid-1)
            else:
                return searchHelper(nums, target, mid+1, end)

        return searchHelper(nums, target, 0, len(nums)-1)

    def search2(self, nums, target):
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    print sol.search(nums, target)
    print sol.search2(nums, target)
    nums = [-1,0,3,5,9,12]
    target = 2
    print sol.search(nums, target)
    print sol.search2(nums, target)
    nums = [-1,0,3,5,9,12]
    target = 13
    print sol.search(nums, target)
    print sol.search2(nums, target)
