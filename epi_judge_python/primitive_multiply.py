from test_framework import generic_test


def multiply(x, y):
    running_sum = 0
    while x:
        if x & 1:
            running_sum = add(running_sum, y)
        x, y = x >> 1, y << 1
    return running_sum

def add(x,y):
    while y:
        carry = x & y
        x, y = x ^ y, carry << 1
    return x

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("primitive_multiply.py",
                                       'primitive_multiply.tsv', multiply))
