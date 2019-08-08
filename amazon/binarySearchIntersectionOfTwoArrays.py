#Author: Madhu Chakravarthy
#Date: 23-03-2018
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        return list(set(nums1) & set(nums2))

    def intersection2(self, nums1, nums2):

        countMap1 = {}

        for num in nums1:
            countMap1[num] = countMap1.get(num, 0) + 1

        countMap2 = {}
        for num in nums2:
            if num in countMap1 and countMap1[num]:
                countMap2[num] = countMap2.get(num,0) + 1
                countMap1[num] -= 1
        import pdb
        pdb.set_trace()
        result = []
        for num, count in countMap2.iteritems():
            if count:
                result.extend([num] * count)

        return result

if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2,2]
    print sol.intersection2(nums1, nums2)
    nums1 = [1]
    nums2 = [1,1]
    print sol.intersection2(nums1, nums2)
    nums1 = [1,1]
    nums2 = [1]
    print sol.intersection2(nums1, nums2)


