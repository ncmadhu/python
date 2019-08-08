#Author: Madhu Chakravarthy
#Date: 22-02-2018
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        sumMap = {}
        for i in A:
            for j in B:
                sum = i + j
                sumMap[sum] = sumMap.get(sum, 0) + 1

        count = 0
        for i in C:
            for j in D:
                sum = i + j
                count += sumMap.get( -1 * sum, 0)

        return count

if __name__ == "__main__":
    sol = Solution()
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    print sol.fourSumCount(A,B,C,D)

