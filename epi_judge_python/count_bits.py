#Author: Madhu Chakravarthy
#Date: 05-08-2019

#Left Shifts
#When shifting left, the most-significant bit is lost, and a 00 bit is inserted on the other end.
#Left shifts multiplies
# 0010 << 1  -  0100
# 0010 << 2  -  1000

#Logical right shift, the least-significant bit is lost and a 0 is inserted on the other end.
#Logical right shift divides
# 1011 >>> 1  -  0101
# 1011 >>> 3  -  0001

#Arithmetic right shift, the least-significant bit is lost and the most-significant bit is copied.
#Artihmetic right shift preserves the sign in twos complement
# 1011 >> 1  -  1101
# 0011 >> 1  -  0001

from test_framework import generic_test


def count_bits(x):
    count = 0
    while x:
        count +=  x & 1
        x = x >> 1
    return count


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("count_bits.py", 'count_bits.tsv',
                                       count_bits))
