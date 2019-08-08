# Author: Madhu Chakravarthy
# Date: 10-01-2018

def fibonacci(number):

    if number == 0:
        return [0]
    if number == 1:
        return [0,1]
    a = 0
    b = 1
    series = [0, 1]
    n = 2
    while n < number:
        a,b = b, a+b
        series.append(b)
        n += 1
    return series

if __name__ == "__main__":
    print fibonacci(9)
    print fibonacci(1)
    print fibonacci(0)


