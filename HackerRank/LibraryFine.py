#!/bin/python
"""
Your local library needs your help! Given the expected and actual return dates for a library book,
create a program that calculates the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0).
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date,
the fine = 15 Hackos x (the number of days late)

If the book is returned after the expected return month but still within the same calendar year as the expected return date,
the fine = 500 Hackos x (the number of months late).
If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos.

Input Format

The first line contains 3 space-separated integers denoting the respective day, month, and year on which the book was actually returned. 
The second line contains 3 space-separated integers denoting the respective day, month, and year on which the book was expected to be returned (due date).

Constraints

1 <= D <= 31
1 <= M <= 12
1 <= Y <= 3000

Output Format

Print a single integer denoting the library fine for the book received as input.

Sample Input

9 6 2015
6 6 2015

Sample Output

45

Explanation

Given the following return dates: 
Actual:  D = 9, M = 6, Y = 2015
Expected: D = 6, M = 6, Y = 2015

Because Expected Year = Actual year, we know it is less than a year late. 
Because Expected Month = Actual Month, we know it's less than a month late. 
Because Expected Date < Actual Date, we know that it was returned late (but still within the same month and year).

Per the library's fee structure, we know that our fine will be 15 Hackos x (# days late).
We then print the result of 15 x (9 -6) = 45 as our output.
"""
import sys


d1,m1,y1 = raw_input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = raw_input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]
fine  = 0
if y1 > y2:
    fine  = 10000
elif m1 > m2 and y1 >= y2:
    fine = (m1 - m2) * 500
elif d1 > d2 and m1 >= m2 and y1 >= y2:
    fine = (d1 - d2) * 15
print fine
