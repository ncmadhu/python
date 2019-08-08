class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 1:
            return length
        else:
            prev = nums[0]
            for num in nums[1:]:
                if num == prev:
                    nums.remove(num)
                else:
                    prev = num
            return len(nums)

if __name__ == "__main__":
    sol =  Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    print sol.removeDuplicates(nums)
