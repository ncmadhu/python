"""
An English text needs to be encrypted using the following encryption scheme. 
First, the spaces are removed from the text. Let L be the length of this text. 
Then, characters are written into a grid, whose rows and columns have the following constraints:

floor(sqrt(L)) <= rows <= column <= ceil(sqrt(L))

For example, the sentence if man was meant to stay on the ground god would have given us roots
after removing spaces is 54 characters long, so it is written in the form of a grid with 7 rows and 8 columns.

ifmanwas  
meanttos          
tayonthe  
groundgo  
dwouldha  
vegivenu  
sroots

Ensure that rows x columns >= L
If multiple grids satisfy the above conditions, choose the one with the minimum area, i.e. rows x columns.
The encoded message is obtained by displaying the characters in a column, inserting a space,
and then displaying the next column and inserting a space, and so on.

For example, the encoded message for the above rectangle is:

imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau

You will be given a message in English with no spaces between the words. The maximum message length can be 81 characters. Print the encoded message.

Here are some more examples:

Sample Input:

haveaniceday

Sample Output:

hae and via ecy

Sample Input:

feedthedog    

Sample Output:

fto ehg ee dd

Sample Input:

chillout

Sample Output:

clu hlt io
"""

#!/bin/python

import sys
import math

s = str(raw_input().strip())

msg_len = len(s)
sqrt = math.sqrt(msg_len)
rows = int(math.floor(sqrt))
columns = int(math.ceil(sqrt))
encoded_str = ''
for i in range(0,columns):
    for j in range(0,rows + 1):
        if i < msg_len:
            encoded_str += s[i]
            i += columns
    encoded_str = encoded_str + " "
print encoded_str.strip()
