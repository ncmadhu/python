#Author: Madhu Chakravarthy
#Date: 15-03-2018
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        start = 1
        end = n
        while start < end:
            mid =  (start + end) / 2
            currVer = isBadVersion(mid)
            if currVer:
                end = mid
            else:
                start = mid + 1
        return start


