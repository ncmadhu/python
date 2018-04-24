#Author: Madhu Chakravarthy
#Date: 23-04-2018
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void
        """
        n = len(matrix)
        for i in range(n/2):
            for j in range(n - n/2):
                val1 = matrix[i][j]
                val2 = matrix[n-1-j][i]
                val3 = matrix[n-1-i][n-1-j]
                val4 = matrix[n-1-(n-1-j)][n-1-i]
                matrix[i][j] = val2
                matrix[n-1-j][i] = val3
                matrix[n-1-i][n-1-j] = val4
                matrix[n-1-(n-1-j)][n-1-i] = val1


if __name__ == "__main__":
    sol =  Solution()
    matrix = [
            [ 5, 1, 9,11],
            [ 2, 4, 8,10],
            [13, 3, 6, 7],
            [15,14,12,16]]
    for row in matrix:
        print row
    sol.rotate(matrix)
    for row in matrix:
        print row
