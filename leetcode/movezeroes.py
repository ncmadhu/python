# Author: Madhu Chakravarthy
# Date: 14-01-2018
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void do not return anything modify in place
        """
        index = 0
        for i in range(len(nums)):
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
            else:
                index += 1

if __name__ == "__main__":
    solution = Solution()
    nums = [0,1,0,3,12]
    solution.moveZeroes(nums)
    print nums
    nums = [0,0,1]
    solution.moveZeroes(nums)
    print nums



