#Author: Madhu Chakravarthy
#Date: 26-02-2018
class Solution(object):
    def solveMaze(self, arr, dest):
        """
        :type arr: List[List[int]]
        :rtype: List[List[int]]
        """
        path = [[0 for i in range(len(arr[0]))] for j in range(len(arr))]
        self.solveMazeRecursive(arr, 0,0, dest, path)
        return path

    def solveMazeRecursive(self, arr, x, y, dest, path):
        if x == dest[0]  and y == dest[1]:
            path[x][y] = 1  
            return True

        if x >=0 and x < len(arr) and y>=0 and y < len(arr[0]) and arr[x][y]:
            path[x][y] = 1

            if self.solveMazeRecursive(arr, x+1, y, dest, path):
                return True
            if self.solveMazeRecursive(arr, x, y+1, dest, path):
                return True
            path[x][y] = 0
            return False

if __name__ == "__main__":
    sol = Solution()
    arr = [[1,0,0,0],
           [1,1,0,1],
           [0,1,0,0],
           [1,1,1,1]]
    dest = [3,3]
    print sol.solveMaze(arr, dest)
