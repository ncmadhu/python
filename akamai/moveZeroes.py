#Author: Madhu Chakravarthy
#Date: 22-04-2018
class Solution(object):
    def moveZeroes2(self, nums):
        length = len(nums)

        nonZeroIndex = 0

        for i in range(length):
            if nums[i] != 0:
                nums[nonZeroIndex] = nums[i]
                nonZeroIndex += 1

        for i in range(nonZeroIndex, length):
            nums[nonZeroIndex] = 0
            nonZeroIndex += 1

    def moveZeroes(self, nums):
        length = len(nums)
        nonZeroIndex = 0
        cur = 0
        while cur < length:
            if nums[cur] != 0:
                nums[nonZeroIndex], nums[cur] = nums[cur], nums[nonZeroIndex]
                nonZeroIndex += 1
            cur += 1



if __name__ == "__main__":
    sol =  Solution()
    nums = [0,1,2,0,2,0,3]
    sol.moveZeroes2(nums)
    print nums
    nums = [0,1,2,0,2,0,3]
    sol.moveZeroes(nums)
    print nums
