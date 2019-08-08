# Enter your code here. Read input from STDIN. Print output to STDOUT
m,n,r = map(int, raw_input().strip().split())
#print m,n,r
matrix = []
for i in range(m):
    matrix.append(raw_input().strip().split())
#print matrix

count = 0
# linearize the array
while (n - count > n / 2) and (m - count > m / 2) :
    top = [(count, i) for i in range(count, n - count, 1)]
    right = [(i, n - 1 - count) for i in range(count + 1, m - 1 - count, 1)]
    bottom = [ ( m - 1 - count, i) for i in range( n - 1 - count, count - 1, -1)]
    left = [( i, count) for i in range(m - 2 - count , count, -1)]

   
    idx_list = top + right + bottom + left
    idx_length = len(idx_list)
    shift_num = r % idx_length
    
    value_list = []
    for i in range(idx_length):
        value_list.append(matrix[idx_list[i][0]][idx_list[i][1]])
    # rotate counter clockwise
    value_list = value_list[shift_num:] + value_list[0:shift_num]
    #print value_list
    
    # susbtitute values in matrix
    for i in range(idx_length):
        matrix[idx_list[i][0]][idx_list[i][1]] = value_list[i]
    #print matrix
    count += 1

for i in range(m):
    row = ''
    for j in range(n):
        row += matrix[i][j] + ' ' 
    row.strip()
    print row