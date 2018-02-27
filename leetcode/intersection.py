# Author: Madhu Chakravarthy
# Date: 14-01-2018

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1 List[int]
        :type nums2 List[int]
        :rtype List[int]
        """
        intersect = []

        length1 = len(nums1)
        length2 = len(nums2)

        if length2 > length1:
            nums1, nums2 = nums2, nums1

        for i in nums1:
            for j,v in enumerate(nums2):
                print j
                if v == i:
                    intersect.append(v)
                    nums2.pop(j)
                    break
        return intersect

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,2,1]
    nums2 = [2,2]
    print solution.intersect(nums1,nums2)
