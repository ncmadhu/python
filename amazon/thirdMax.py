#Author: Madhu Chakravarthy
#Date: 09-02-2018

class Solution(object):
    def thirdMax(self, nums):
        max1 = None
        max2 = None
        max3 = None

        for num in nums:
            if num == max1 or num == max2 or num == max3:
                continue
            if num > max1 or max1 == None:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2 or max2 == None:
                max3 = max2
                max2 = num
            elif num > max3 or max3 == None:
                max3 = num
        return max3 if max3 != None else max1

if __name__ == "__main__":
    sol = Solution()
    """
    arr = [1,2,2,3]
    print sol.thirdMax(arr)
    """
    arr = [3,3,4,3,4,3,0,3,3]
    print sol.thirdMax(arr)

