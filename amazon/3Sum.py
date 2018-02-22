#Author: Madhu Chakravarthy
#Date: 09-02-2018
class Solution(object):
    def threeSum(self, nums):
        result = set()
        nums.sort()
        length = len(nums)
        for i in range(length-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i+1
            r = length - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    result.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
                    r -= 1
        return result

if __name__ == "__main__":
    sol = Solution()
    arr = [-1,0,1,2,-1,-4]
    print sol.threeSum(arr)


