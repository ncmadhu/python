#Author: Madhu Chakravarthy
#Date: 27-02-2018

class Position(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
    
class Solution(object):
    def solveNQueenProblem(self, n):
        """
        :type n int
        :rtype List[Position]
        """
        #initialize the positions array
        positions = [Position(0,0) for i in range(n)]

        if self.solveNQueenUtil(n, 0, positions):
            print "Solution acheived"
            return positions
        else:
            print "No Solution"
            return positions

    def solveNQueenUtil(self, n, row, positions):
        #check whether n rows has been reached
        #if its reached return True
        if n == row:
            return True

        for col in range(n):
            foundPosition = True
            #check previous queens are stationed in any of the
            #same col either vertically or diagonally
            for queen in range(row):
                if positions[queen].col == col or \
                   positions[queen].row + positions[queen].col == row + col or \
                   positions[queen].row - positions[queen].col == row - col:
                       foundPosition = False
                       break
            if foundPosition:
                #mark the position of the queen
                positions[row] = Position(row, col)
                #move to next queen
                if self.solveNQueenUtil(n, row+1, positions):
                    return True
        #If no position for current queen backtrack
        return False

    def printPositions(self, positions):
        for queen, position in enumerate(positions, 1):
            print "queen %d position: %d,%d" % (queen, position.row, position.col)

if __name__ == "__main__":
    sol =  Solution()
    positions = sol.solveNQueenProblem(4)
    sol.printPositions(positions)
    positions = sol.solveNQueenProblem(8)
    sol.printPositions(positions)



