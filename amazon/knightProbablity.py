#Author: Madhu Chakravarthy
#Date: 27-02-2018
class Solution(object):
    def knightProbablity(self, n, k, r, c):
        """
        :type n: int
        :type k: int
        :type r: int
        :type c: int
        :rtype: float
        """
        #Initialize n * n array with 0 
        dp = [[0] * n for _ in range(n)]
        dp[r][c] = 1

        #move k steps
        for _ in xrange(k):
            #initialize next step array 
            dp2 = [[0] * n for _ in range(n)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in ((2,1), (1,2), (-1,2),(-2,1),
                                   (-2,-1),(-1,-2),(1,-2),(2,-1)):
                        if 0 <= r + dr < n and 0 <= c + dc < n:
                            dp2[r+dr][c+dc] += val / 8.0
            print dp2
            dp = dp2

        print dp
        return sum(map(sum,dp))

if __name__ == "__main__":
    sol = Solution()
    print sol.knightProbablity(3, 2, 0, 0)

        
