#Author: Madhu Chakravarthy
#Date: 20-04-2018
class Solution(object):
    def rotate(self, nums, k):
        length = len(nums)
        k = k % length
        count  = 0
        for j in range(length): 
            start = i = j
            prev =  nums[i]
            while True:
                i = (i+k) % length
                nums[i], prev =  prev, nums[i]
                count += 1
                if i == start:
                    print i
                    break
            if count >= length:
                break



if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4,5,6,7]
    sol.rotate(nums, 3)
    print nums
    nums = [1,2,3,4,5,6]
    sol.rotate(nums, 3)
    print nums
