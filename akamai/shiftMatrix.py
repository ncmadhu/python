#Author: Madhu Chakravarthy
#Date: 17-04-2018

def shiftMatrix(matrix, k):

    print matrix
    for index, row in enumerate(matrix):
        matrix[index] = row[k:] + row[0:k]

    print matrix

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    shiftMatrix(matrix, 2)
    matrix = [[3,4,1,2], [7,8,5,6],[11,12,9,10]]
    shiftMatrix(matrix, 2)


