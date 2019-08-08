# Author: Madhu Chakravarthy
# Date: 14-01-2018

class Solution(object):
    def singleNumber(self,nums):
        """
        :type nums List[int]
        :rtype int
        """
        a = 0
        for i in nums:
            a = a^i
        return a

if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,2,3,4,3,4]
    print solution.singleNumber(nums)
    nums = [1,1,2]
    print solution.singleNumber(nums)
