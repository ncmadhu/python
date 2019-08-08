#!/bin/python

"""
Little Bobby loves chocolate, and he frequently goes to his favorite 5&10 store, Penny Auntie, with n dollars to buy chocolates.
Each chocolate has a flat cost of c dollars, and the store has a promotion where they allow you to trade in m chocolate wrappers
in exchange for 1 free piece of chocolate.

For example, if m = 2 and Bobby has n = 4 dollars that he uses to buy 4 chocolates at c = 1 dollar apiece,
he can trade in the 4 wrappers to buy 2 more chocolates. Now he has 2 more wrappers that he can trade in for 1 more chocolate.
Because he only has 1 wrapper left at this point and 1 < m, he was only able to eat a total of 5 pieces of chocolate.

Given n, c, and m for t trips to the store, can you determine how many chocolates Bobby eats during each trip?

Input Format

The first line contains an integer, t, denoting the number of trips Bobby makes to the store. 
Each line i of the t subsequent lines contains three space-separated integers describing the respective n, c, and m values
for one of Bobby's trips to the store.

Constraints

1 <= t <= 1000
2 <= n <= 10^5
1 <= c <= n
2 <= m <=n

Output Format

For each trip to Penny Auntie, print the total number of chocolates Bobby eats on a new line.

Sample Input

3
10 2 5
12 4 4
6 2 2

Sample Output

6
3
5

Explanation

Bobby makes the following  trips to the store:

He spends his 10 dollars on 5 chocolates at 2 dollars apiece. He then eats them and exchanges all 5 wrappers to get 1 more chocolate.
We print the total number of chocolates he ate, which is 6.

He spends his 12 dollars on 3 chocolates at 4 dollars apiece; however, he needs 4 wrappers to trade for his next chocolate.
Because he only has 3 wrappers, he cannot purchase or trade for any more chocolates. We print the total number of chocolates he ate, which is 3.

He spends 6 dollars on 3 chocolates at 2 dollars apiece. He then exchanges 2 of the 3 wrappers for 1 additional piece of chocolate.
Next, he uses his third leftover chocolate wrapper from his initial purchase with the wrapper from his trade-in to do a second trade-in for 1 more piece
of chocolate. At this point he has 1 wrapper left, which is not enough to perform another trade-in. We print the total number of chocolates he ate, which is 5.

"""

import sys

def getchoclate(num_wrap, wraps_per_choc):
    if num_wrap > 0:
        free_ch = num_wrap / wraps_per_choc
        rem_wrap = num_wrap % wraps_per_choc
        total_wraps = free_ch + rem_wrap
        if total_wraps >= wraps_per_choc:
            return free_ch + getchoclate(total_wraps, wraps_per_choc)
        else:
            return free_ch
    else:
        return 0

t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    chocs = n / c
    total_choc = chocs + getchoclate(chocs,m)
    print total_choc