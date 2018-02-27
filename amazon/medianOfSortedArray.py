#Author: Madhu Chakravarthy
#Date: 22-02-2018

from __future__ import division
import sys

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        nums1_len = len(nums1)
        nums2_len = len(nums2)

        '''
        if nums1_len == 0:
            partition = nums2_len // 2
            if nums2_len % 2 == 0:
                return (nums2[partition - 1] + nums2[partition]) / 2
            else:
                return nums2[partition]
        '''
        low = 0
        high = nums1_len

        while low <= high:

            partition_nums1 = (low + high) // 2
            partition_nums2 = (nums1_len + nums2_len + 1) // 2 - partition_nums1

            max_left_nums1 = -sys.maxint - 1 if partition_nums1 == 0 else nums1[partition_nums1 - 1]
            min_right_nums1 = sys.maxint if partition_nums1 == nums1_len else nums1[partition_nums1]

            max_left_nums2 = -sys.maxint - 1 if partition_nums2 == 0 else nums2[partition_nums2 - 1]
            min_right_nums2 = sys.maxint if partition_nums2 == nums2_len else nums2[partition_nums2]

            if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
                if (nums1_len + nums2_len) % 2 == 0:
                    return (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) / 2.0
                return float(max(max_left_nums1, max_left_nums2))
            elif max_left_nums1 > min_right_nums2:
                high = partition_nums1 - 1
            else:
                low = partition_nums1 + 1

if __name__ == "__main__":
    sol = Solution()
    '''
    nums1 = [1,3,8,9,15]
    nums2 = [7,11,18,19,21,25]
    print sol.findMedianSortedArrays(nums1, nums2)
    nums1 = [1,2]
    nums2 = [3,4]
    print sol.findMedianSortedArrays(nums1, nums2)
    nums1 = [1,3]
    nums2 = [2]
    print sol.findMedianSortedArrays(nums1, nums2)
    nums1 = [1]
    nums2 = [1]
    print sol.findMedianSortedArrays(nums1, nums2)
    '''
    nums1 = [2]
    nums2 = []
    print sol.findMedianSortedArrays(nums1, nums2)






