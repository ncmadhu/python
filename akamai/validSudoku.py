#Author: Madhu Chakravarthy
#Date: 22-04-2018
class Solution(object):
    def isValidSudoku(self, board):
        rowDict = {}
        colDict = {}
        for i in range(9):
            rowDict[i] = []
            colDict[i] = []
        i = 0
        while i < 9:
            j = 0
            while j < 9:
                subBoard = []
                for row in range(i, i+3):
                    for col in range(j, j+3):
                        num = board[row][col]
                        if num == '.':
                            continue
                        elif num in subBoard or num in rowDict[row] or num in colDict[col]:
                            return False
                        else:
                            subBoard.append(num)
                            rowDict[row].append(num)
                            colDict[col].append(num)
                j += 3
            i += 3
        return True
    
    def isValidSudoku2(self, board):
        seen = sum(([(c, i), (j, c), (i/3, j/3, c)]
                for i, row in enumerate(board)
                for j, c in enumerate(row)
                if c != '.'), [])
        print seen
        return len(seen) == len(set(seen))


if __name__ == "__main__":
    sol =  Solution()
    board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    print sol.isValidSudoku(board)
    board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    print sol.isValidSudoku(board)
    board = [
 ["8","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]]
    print sol.isValidSudoku(board)
    print sol.isValidSudoku2(board)
