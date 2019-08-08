#Author: Madhu Chakravarthy
#Date: 01-03-2018
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        versions1 = map(int, version1.split('.'))
        versions2 = map(int, version2.split('.'))

        len1 = len(versions1)
        len2 = len(versions2)

        import pdb
        pdb.set_trace()
        for i in range(max(len1, len2)):
            v1 = versions1[i] if i < len1 else 0
            v2 = versions2[i] if i < len2 else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0

if __name__ == "__main__":
    sol = Solution()
    version1 = '0.1'
    version2 = '1.1'
    print sol.compareVersion(version1, version2)
    version1 = '1'
    version2 = '0'
    print sol.compareVersion(version1, version2)
    version1 = '1.0.1'
    version2 = '0'
    print sol.compareVersion(version1, version2)
    version1 = '1'
    version2 = '01'
    print sol.compareVersion(version1, version2)
