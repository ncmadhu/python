#Author: Madhu Chakravarthy
#Date: 08-03-2018
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Initialize both at the start of the list
        tortoise = nums[0]
        hare = nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise ==  hare:
                break

        ptr1 = nums[0]
        ptr2 = hare

        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1

if __name__ == "__main__":
    sol =  Solution()
    nums = [1,4,6,6,6,2,3]
    print sol.findDuplicate(nums)
