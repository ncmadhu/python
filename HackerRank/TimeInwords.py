#!/bin/python

"""
Given the time in numerals we may convert it into words, as shown below:

5:00 -- > five o' clock
5:01 -- > one minute past five
5:10 -- > ten minutes past five
5:30 -- > half past five
5:40 -- > twenty minutes to six
5:45 -- > quarter to six
5:47 -- > thirteen minutes to six
5:28 --> twenty eight minutes past five

Write a program which prints the time in words for the input given in the format mentioned above.

Input Format

There will be two lines of input:
H, representing the hours
M, representing the minutes

Constraints
1 <= H <= 12
0 <= M <= 60
0 <= M <= 60

Output Format

Display the time in words.

Sample Input

5  
47  
Sample Output

thirteen minutes to six
"""

import sys


h = int(raw_input().strip())
m = int(raw_input().strip())
number_in_words = {1 : "one", 2 : "two", 3 : "three", 4: "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine", 10 : "ten", 11 : "eleven", 12 : "twelve", 13 : "thirteen", 14 : "fourteen", 15 : "fifteen", 16 : "sixteen", 17 : "seventeen", 18 : "eighteen", 19 : "nineteen", 20 : "twenty", 21 : "twenty one", 22 : "twenty two", 23 : "twenty three", 24 : "twenty four", 25 : "twenty five", 26 : "twenty six", 27 : "twenty seven", 28 : "twenty eight", 29 : "twenty nine", 30 : "thirty"}

before_30_string = " minutes past "
after_30_string = " minutes to "
output_string = ''
if m == 0:
    output_string = number_in_words[h] + " o' clock"
elif m== 1:
    output_string = "one minute past " + number_in_words[h]
elif m <= 30:
    if m == 30:
        output_string = "half past " + number_in_words[h]
    elif m == 15:
        output_string = "quarter past " + number_in_words[h]
    else:
        output_string = number_in_words[m] + before_30_string + number_in_words[h]
elif m > 30:
    if h == 12:
        h = 1
    else:
        h = h + 1
    if m == 45:
        output_string = "quarter to " + number_in_words[h]
    else:
        m = 60 - m
        output_string = number_in_words[m] + after_30_string + number_in_words[h]
print output_string