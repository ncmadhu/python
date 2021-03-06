#!/bin/python

"""
You are given a square map of size n x n. Each cell of the map has a value denoting its depth.
We will call a cell of the map a cavity if and only if this cell is not on the border of the map
and each cell adjacent to it has strictly smaller depth. Two cells are adjacent if they have a common side (edge).

You need to find all the cavities on the map and depict them with the uppercase character X.

Input Format

The first line contains an integer, n, denoting the size of the map. Each of the following n lines contains n positive digits without spaces.
Each digit (1-9) denotes the depth of the appropriate area.

Constraints 

1 <= n <= 100

Output Format

Output n lines, denoting the resulting map. Each cavity should be replaced with character X.

Sample Input

4
1112
1912
1892

Sample Output

1112
1X12
18X2
1234

Explanation

The two cells with the depth of 9 fulfill all the conditions of the Cavity definition and have been replaced by X.
"""

import sys


n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
    grid_t = str(raw_input().strip())
    grid.append(grid_t)
for i in range(1,n-1):
    for j in range(1,n-1):
        value = grid[i][j]
        edge_list = [grid[i-1][j],grid[i+1][j],grid[i][j-1],grid[i][j+1]]
        if value > max(edge_list):
            new_str = ''
            old_str = grid[i]
            new_str = old_str[0:j] + 'X' + old_str[j+1:]
            grid[i] = new_str
for i in grid:
    print i