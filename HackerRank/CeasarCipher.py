#!/bin/python

"""
Julius Caesar protected his confidential information by encrypting it in a cipher.
Caesar's cipher rotated every letter in a string by a fixed number, K, making it unreadable by his enemies.
Given a string, S, and a number, K, encrypt S and print the resulting string.

Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

Input Format

The first line contains an integer, N, which is the length of the unencrypted string. 
The second line contains the unencrypted string, S. 
The third line contains the integer encryption key, K, which is the number of letters to rotate.

Constraints 

1 <= N <= 100
0 <= K <= 100 
S is a valid ASCII string and doesn't contain any spaces.

Output Format

For each test case, print the encoded string.

Sample Input

11
middle-Outz
2

Sample Output

okffng-Qwvb

Explanation

Each unencrypted letter is replaced with the letter occurring K spaces after it when listed alphabetically.
Think of the alphabet as being both case-sensitive and circular; if K rotates past the end of the alphabet,
it loops back to the beginning (i.e.: the letter after z is a, and the letter after Z is A).

Selected Examples: 
m (ASCII 109) becomes o (ASCII 111). 
i (ASCII 105) becomes k (ASCII 107). 
- remains the same, as symbols are not encoded. 
O (ASCII 79) becomes Q (ASCII 81). 
z (ASCII 122) becomes b (ASCII 98); because z is the last letter of the alphabet, a (ASCII 97) is the next letter after it in lower-case rotation.
"""
import sys

def get_ascii_value(ascii_value, max_val, min_val):
    if ascii_value > max_val:
        new_ascii = (ascii_value % max_val) + min_val
        return get_ascii_value(new_ascii, max_val, min_val)
    else:
        return ascii_value
    

n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())
cap_list = range(65,91)
small_list = range(97,123)
new_str = ''
for i in range(n):
    ascii_value = ord(s[i])
    if ascii_value in cap_list or ascii_value in small_list:
        if ascii_value in cap_list:
            max_ascii_value = 90
            min_ascii_value = 64
        else:
            max_ascii_value = 122
            min_ascii_value = 96
        new_ascii = get_ascii_value(ascii_value + k, max_ascii_value, min_ascii_value)
        #print ascii_value
        #print new_ascii
        new_str += chr(new_ascii)
    else:
        new_str += s[i]
print new_str