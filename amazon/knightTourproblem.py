#Author: Madhu Chakravarthy
#Date: 26-02-2018
class Solution(object):

    #Initialize array size
    arrX = 8
    arrY = 8

    def solveKnightTour(self):
        """
        :rtype List[List[int]]
        """

        #Initialize the moves array with -1
        #-1 represents non visited square
        sol = [[-1 for j in range(self.arrY)] for i in range(self.arrX)]
        #Initialize the possible moves knight can take
        possibleMoves = [[2,1],
                         [1,2],
                         [-1,2],
                         [-2,1],
                         [-2,-1],
                         [-1,-2],
                         [1,-2],
                         [2,-1]]
        sol[0][0] = 0


        if self.solveKnightUtil(0, 0, 1, possibleMoves, sol):
            return sol
        else:
            print "Solution doesnt exist"
            return sol

    def isSafe(self, x, y, sol):
        """
        See wether x and y is in bounds and not visited before
        """
        if x >= 0 and x < self.arrX and y >=0 and y < self.arrY and sol[x][y] == -1:
            return True
        else:
            return False

    def solveKnightUtil(self, x, y, move, possibleMoves, sol):
        """
        Move the knight until it reaches maximum possible
        moves are reached for the given arrX * arrY
        """
        if move == self.arrX * self.arrY:
            return True

        """
        Move the knight from current position x, y
        to the nextX and nextY with one of possibleMoves
        """

        for option in possibleMoves:

            nextX = x + option[0]
            nextY = y + option[1]

            if self.isSafe(nextX, nextY, sol):
                sol[nextX][nextY] = move
                if self.solveKnightUtil(nextX, nextY, move+1, possibleMoves, sol):
                    return True
                else:
                    sol[nextX][nextY] = -1 # backtrack
        return False
                




if __name__ == "__main__":
    sol =  Solution()
    solArr = sol.solveKnightTour()
    for row in solArr:
        print row
        

