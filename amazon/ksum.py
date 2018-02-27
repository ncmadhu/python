#Author: Madhu Chakravarthy
#Date: 21-02-2018
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def findNSum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
                return
            if N == 2:
                l,r = 0, len(nums)-1
                while l < r:
                    sum = nums[l] + nums[r]
                    if sum == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif sum < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                        findNSum(nums[i+1:], target - nums[i], N-1, result + [nums[i]], results)
        results = []
        findNSum(sorted(nums), target, 4, [], results)
        return results

if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    sol = Solution()
    print sol.fourSum(nums, 0)

