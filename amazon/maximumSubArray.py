#Author: Madhu Chakravarthy
#Date: 1-03-2018
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #initialize total, subArrayCount and total map
        total = 0
        subArrayCount = 0
        #Its set as -1 if sum not present return -1
        totalMap = {0: -1}

        for i in xrange(len(nums)):
            total += nums[i]

            #check total already present before updating
            #total at the index position
            if total not in totalMap:
                totalMap[total] = i

            #check diff of total k is present in totalMap
            #if present. if present K is in between those indexes
            if total - k in totalMap:
                subArrayCount = max(subArrayCount, i - totalMap[total - k])

        return subArrayCount

if __name__ == "__main__":
    sol =  Solution()
    nums = [1,-1,5,-2,3]
    k = 3
    print sol.maxSubArrayLen(nums, k)


