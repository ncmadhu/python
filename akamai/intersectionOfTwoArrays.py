#Author: Madhu Chakravarthy
#Date: 22-04-2018
class Solution(object):
    def intersect(self, nums1, nums2):
        countMap1 = {}
        for num in nums1:
            countMap1[num] = countMap1.get(num, 0) + 1

        countMap2 = {}
        for num in nums2:
            if num in countMap1 and countMap1[num]:
                countMap2[num] = countMap2.get(num, 0) + 1
                countMap1[num] -= 1

        result = []
        for num, count in countMap2.iteritems():
            if count:
                result.extend([num] * count)

        return result

if __name__ == "__main__":
    sol =  Solution()
    print sol.intersect([1,2,2,1], [2,2])
