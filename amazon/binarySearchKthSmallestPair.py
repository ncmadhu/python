#Author: Madhu Chakravarthy
#Date: 24-03-2018
import heapq

class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        heap = [(nums[i+1] - nums[i], i, i+1) for i in xrange(len(nums) - 1)]
        heapq.heapify(heap)

        for _ in xrange(k):
            d, root, nei =  heapq.heappop(heap)
            if nei + 1 < len(nums):
                heapq.heappush(heap, (nums[nei+1] - nums[root], root, nei+1))

        return d

    def smallestDistancePair2(self, nums, k):

        def possible(guess):
            count = left = 0
            for index, value in enumerate(nums):
                while value - nums[left] > guess:
                    left += 1
                count += index - left
            return count >= k

        nums.sort()
        low = 0
        high = nums[-1] - nums[0]

        while low < high:
            mid = (low + high) / 2
            if possible(mid):
                high = mid
            else:
                low = mid + 1
        return low

if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,1]
    print sol.smallestDistancePair(nums,1)
    print sol.smallestDistancePair2(nums,1)
    nums = [1,3,1]
    print sol.smallestDistancePair(nums,2)
    print sol.smallestDistancePair2(nums,2)
    
