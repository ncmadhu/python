#Author: Madhu Chakravarthy
#Date: 09-05-2018
class Solution(object):
    def ticTacToeWinner(self, gameBoard):

        # get length of board
        # row and column length are same since its n x n
        colLength = rowLength = len(gameBoard)

        gameStarter = self.findStarter(gameBoard, rowLength, colLength)
        #check if all the elemnts in a row are same to guess winner
        winner = self.checkRowMatch(gameBoard, rowLength, colLength)
        if winner:
            return gameStarter, winner
        
        #check if all the elements in a column are same to guess winner
        winner = self.checkColumnMatch(gameBoard, rowLength, colLength)
        if winner:
            return gameStarter, winner
        
        #check if all the elements diagonally from top left to bottom right are same
        winner = self.checkTopLeftDiagonalMatch(gameBoard, rowLength, colLength)
        if winner:
            return gameStarter, winner
        
        #check if all the elements diagonally from top right to bottom left are same
        winner = self.checkTopRightDiagonalMatch(gameBoard, rowLength, colLength)
        if winner:
            return gameStarter, winner


        return gameStarter,'D'

    def checkRowMatch(self, gameBoard, rowLength, colLength):
        # check consecutive elements in a row are same
        #. . .
        #X X X
        #. . .

        winner = None
        for row in range(rowLength):
            winnerFound =  True
            for col in range(colLength-1):
                if gameBoard[row][col] == gameBoard[row][col+1]:
                    #continue if next element in the row is same
                    continue
                else:
                    #break from loop if next element is not the same
                    winnerFound =  False
                    break
            if winnerFound:
                #since in row all the elements are the same using 0 index postion to get
                #the winner
                winner = gameBoard[row][0]
                if winner == 'U':
                    continue
                #winner found hence no need to check rest of the rows
                break

        return winner

    def checkColumnMatch(self, gameBoard, rowLength, colLength):
        #check consecutive elements in a column are same
        #X . .
        #X . .
        #X . .

        winner = None
        for col in range(colLength):
            winnerFound = True
            for row in range(rowLength-1):
                if gameBoard[row][col] == gameBoard[row+1][col]:
                    #continue if next element in the column is same
                    continue
                else:
                    #break from loop is next element is not the same
                    winnerFound = False
                    break
            if winnerFound:
                #since in column all the elements are same using 0 index position to get
                #the winner
                winner =  gameBoard[0][col]
                if winner == 'U':
                    continue
                #winner found hence no need to check rest of the columns
                break

        return winner

    def checkTopLeftDiagonalMatch(self, gameBoard, rowLength, colLength):
        #check elements are same diagonally from top left to bottom right
        #X . .
        #. X .
        #. . X
       

        winner =  None
        winnerFound = True
        #For diagonal check row and columnf index will be same
        #hence no nested loop
        for index in range(rowLength - 1):
            if gameBoard[index][index] == gameBoard[index+1][index+1]:
                continue
            else:
                winnerFound = False
                break

        if winnerFound:
            winner =  gameBoard[0][0]

        return winner

    def checkTopRightDiagonalMatch(self, gameBoard, rowLength, colLength):
        #check elements are same diagonally from top right to bottom left
        #. . X
        #. X .
        #X . .

        winner =  None
        winnerFound = True

        #start from end and decrement by one every iteration until reaches zero
        #start, end, incrementByValue ----> rowLength-1, 0, -1
        for index in range(rowLength - 1, 0, -1):
            if gameBoard[index][index] == gameBoard[index-1][index-1]:
                continue
            else:
                winnerFound = False
                break

        if winnerFound:
            winner =  gameBoard[0][0]

        return winner

    def findStarter(self, gameBoard, rowLength, colLength):
        playerDict = {'X': 0, 'O': 0, 'U': 0}

        for row in range(rowLength):
            for col in range(colLength):
                playerDict[gameBoard[row][col]] += 1

        gameStarter = 'X' if playerDict['X'] > playerDict['O'] else 'O'

        return gameStarter 


if __name__ == "__main__":
    sol =  Solution()
    """
    gameBoard = ['XXO', 'OOX', 'XOO']
    print sol.ticTacToeWinner(gameBoard)
    gameBoard = ['OXO', 'XXX', 'XOX']
    print sol.ticTacToeWinner(gameBoard)
    gameBoard = ['XOO', 'OOX', 'XOX']
    print sol.ticTacToeWinner(gameBoard)
    gameBoard = ['OOX', 'XOX', 'XOO']
    print sol.ticTacToeWinner(gameBoard)
    gameBoard = ['XOX', 'OXO', 'XOX']
    print sol.ticTacToeWinner(gameBoard)
    gameBoard = ['XOX', 'OXO', 'OXO']
    print sol.ticTacToeWinner(gameBoard)
    """
    gameBoard = ['XOX', 'XXO', 'OOX']
    print sol.ticTacToeWinner(gameBoard)
    gameBoard = ['XOX', 'OXO', 'OXO']
    print sol.ticTacToeWinner(gameBoard)
    gameBoard = ['OOX', 'OXX', 'OUU']
    print sol.ticTacToeWinner(gameBoard)
    gameBoard = ['UOXU', 'UOXU', 'UOXU', 'UOUU']
    print sol.ticTacToeWinner(gameBoard)



