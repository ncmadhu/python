# Author: Madhu Chakravarthy
# Date: 14-01-2018
class Solution(object):

    def twoSum(self, nums, target):
        map = {}
        for i,v in enumerate(nums):
            complement =  target - v
            if complement in map:
                return [map[complement],i]
            map[v] = i

    def twoSum3(self, nums, target):
        length = len(nums)

        for i in range(length):

            for k in range(0,i):
                if nums[k] + nums[i] == target:
                    return [k, i]
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i,j]

    def twoSum2(self, nums, target):
        """
        :type nums List[int]
        :type target int
        :rtype List[int]
        """
        length = len(nums)
        for i in range(length):
            x = nums.pop(0)
            for y in nums:
                if x + y  == target:
                    return [x,y]

if __name__ == "__main__":
    solution = Solution()
    nums = [2,7,11,15]
    target = 9
    print solution.twoSum(nums, target)
