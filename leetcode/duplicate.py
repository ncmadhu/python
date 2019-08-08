# Author: Madhu Chakravarthy
# Date: 14-01-2018

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype bool
        """
        duplicate = False
        numKeys = {}
        for num in nums:
            if num in numKeys:
                duplicate = True
                break
            else:
                numKeys[num] = True
        return duplicate

if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,2,3,4]
    print solution.containsDuplicate(nums)
    nums = [1]
    print solution.containsDuplicate(nums)
    nums = [1,2,3,4,5,6]
    print solution.containsDuplicate(nums)

