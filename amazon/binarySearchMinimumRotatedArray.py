#Author: Madhu Chakravarthy
#Date: 22-03-2018
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        start = 0
        end =  len(nums) - 1

        while start < end:
            mid = (start + end) / 2
            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[end]:
                end = mid
            else:
                end -= 1

        return nums[start]

if __name__ == "__main__":
    sol = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    print sol.findMin(nums)
    nums = [1,2,3,4,5,6,7]
    print sol.findMin(nums)
    nums = [1,2,2,3,3,4,5,6,7]
    print sol.findMin(nums)
    nums = [4,5,6,7,7,0,0,1,2]
    print sol.findMin(nums)
