#Author: Madhu Chakravarthy
#Date: 20-04-2018
class Solution(object):
    def containsDuplicate(self, nums):
        numsDict = {}
        for num in nums:
            if num in numsDict:
                return True
            numsDict[num] = 1
        return False

if __name__ == "__main__":
    sol =  Solution()
    print sol.containsDuplicate([1,2,3,4,5])
    print sol.containsDuplicate([1,2,3,4,4,5])
