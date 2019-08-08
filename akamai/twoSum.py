#Author: Madhu Chakravarthy
#Date: 22-04-2018
class Solution(object):
    def twoSum(self, nums, target):
        numMap = {}
        for index, num in enumerate(nums):
            if (target - num) in numMap:
                return [numMap[target-num], index]
            numMap[num] = index

if __name__ == "__main__":
    sol =  Solution()
    print sol.twoSum([2, 7, 11, 15], 9)
