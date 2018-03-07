#Author: Madhu Chakravarthy
#Date: 02-03-2018

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        length = len(nums)
        p = 1
        output = []
        for i in range(length):
            output.append(p)
            p = p * nums[i]

        p = 1

        for i in range(length-1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4]
    print sol.productExceptSelf(nums)

