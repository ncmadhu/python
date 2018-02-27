# Author: Madhu Chakravarthy
# Date: 12-01-2018

class Solution(object):
    def rotate(self, nums, k):
        """
        type: nums List[int]
        type: k int
        rtype: void Do not return anything
        """
        length = len(nums)
        k = k % length
        count = 0
        start = 0
        while count < length:
            current = start
            temp = nums[current]
            while True:
                index = (current + k) % length
                nums[index], temp = temp, nums[index]
                current = index
                count += 1
                if current == start:
                    break
            start += 1


if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,4,5,6,7]
    solution.rotate(nums,3)
    print nums
    nums = [1,2]
    solution.rotate(nums,1)
    print nums
    nums = [1,2,3,4,5,6]
    solution.rotate(nums,2)
    print nums

