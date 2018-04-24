#Author: Madhu Chakravarthy
#Date: 20-04-2018
class Solution(object):
    def singleNumber(self, nums):
        a = 0
        for num in nums:
            a ^= num
        return a

if __name__ == "__main__":
    sol =  Solution()
    print sol.singleNumber([2,2,1])
    print sol.singleNumber([1,2,2])
    print sol.singleNumber([4,1,2,1,2])
