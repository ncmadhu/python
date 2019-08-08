#Author: Madhu Chakravarthy
#Date: 25-03-2018
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        if len(nums) == 2:
            return nums[0] if nums[0] > nums[1] else nums[1]

        curr_diff = abs(nums[0] - sum(nums[1:]))
        split_indx = 1

        for i in range(2, len(nums) - 1):
            diff = abs(sum(nums[0:i]) - sum(nums[i:]))
            if diff < curr_diff:
                curr_diff = diff
                split_indx = i

        sum_left = sum(nums[0:split_indx])
        sum_right = sum(nums[split_indx:])

        return sum_left if sum_left > sum_right else sum_right

    def splitArray2(self, nums, m):

        def canSplit(nums, maxVal, m):

            currSum = 0
            subArrCount = 1

            for n in nums:
                currSum += n
                if currSum > maxVal:
                    currSum = n
                    subArrCount += 1
                    if subArrCount > m:
                        return False
            return True

        length = len(nums)

        if m == length:
            return max(nums)
        if m == 1:
            return sum(nums)

        low = max(nums)
        high = sum(nums)

        while low < high:
            mid = (low + high) / 2

            if canSplit(nums, mid, m):
                high = mid
            else:
                low = mid + 1

        return low

if __name__ == "__main__":
    sol = Solution()
    nums = [7,2,5,10,8]
    print sol.splitArray(nums, 2)
    print sol.splitArray2(nums, 2)




