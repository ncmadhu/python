#Author: Madhu Chakravarthy
#Date: 17-04-2018
def fibonacci(n):
    if n <= 1:
        return n
    else:
        a = 0
        b = 1

        i = 2

        while i <= n:
            c = a + b
            a = b
            b = c
            i += 1

        return c

def fibonacciSeries(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0,1]
    elif n == 2:
        return [0,1,1]
    else:
        series = [0,1,1]
        a = 1
        b = 1
        i = 3
        while i <= n:
            c =  a + b
            a = b
            b = c
            i += 1
            series.append(c)
        return series


if __name__ == "__main__":
    print fibonacci(0)
    print fibonacci(1)
    print fibonacci(2)
    print fibonacci(3)
    print fibonacci(4)
    print fibonacci(5)
    print fibonacci(6)
    print fibonacci(7)
    print fibonacci(8)
    print fibonacci(9)
    print fibonacciSeries(9)
    print fibonacciSeries(0)
    print fibonacciSeries(1)
    print fibonacciSeries(2)

