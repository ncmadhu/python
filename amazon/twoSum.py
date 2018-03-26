#Author: Madhu Chakravarthy
#Date: 23-03-2018
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        numMap = {}
        for index, num in enumerate(numbers):
            if target - num in numMap:
                return [numMap[target - num], index + 1]
            else:
                numMap[num] = index + 1

if __name__ == "__main__":
    sol = Solution()
    numbers = [2,7,11,15]
    target = 9
    print sol.twoSum(numbers, target)
