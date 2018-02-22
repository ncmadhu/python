#Author: Madhu Chakravarthy
#Date: 07-02-2018
class Solution(object):
    def longestSquare(self, arr):
        arrCopy = arr
        maxSquare = 0
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if i == 0 or j == 0:
                    continue
                elif arr[i][j] > 0:
                    arrCopy[i][j] = 1 + min(arrCopy[i][j-1],
                                        arrCopy[i-1][j],
                                        arrCopy[i-1][j-1])
                if arrCopy[i][j] > maxSquare:
                    maxSquare = arrCopy[i][j]
        return maxSquare


if __name__ == "__main__":
    sol = Solution()
    arr = [[1,1,0,1,0],[0,1,1,1,0],[1,1,1,1,0],[0,1,1,0,1]]
    print sol.longestSquare(arr)
    arr = [[1,1,0,1,0],[0,1,1,1,1],[1,1,1,1,1],[0,1,1,1,1]]
    print sol.longestSquare(arr)
