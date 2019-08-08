#!/bin/python

"""
Given a time in AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00 AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00 PM on a 12-hour clock,
and 12:00:00 on a 24-hour clock.

Input Format

A single string containing a time in 12-hour clock format (i.e. hh:mm:ssAM  or hh:mm:ssPM ),
where 01 <= hh <= 12.

Output Format

Convert and print the given time in 24-hour format, where 00 <= hh <= 23.

Sample Input

07:05:45PM

Sample Output

19:05:45

"""

import sys
import re

time = raw_input().strip()
pattern = re.compile("^([0-9]{2}):([0-9]{2}):([0-9]{2})(AM|PM)$")
match = pattern.findall(time)
hour = ""
if match:
    if match[0][3] == "AM":
        if int(match[0][0]) == 12:
            hour = "00"
        else:
            hour = match[0][0]
    else:
        if int(match[0][0]) == 12:
            hour = match[0][0]
        else:
            hour = str(int(match[0][0]) + 12)
print hour + ":" + match[0][1] + ":" + match[0][2]