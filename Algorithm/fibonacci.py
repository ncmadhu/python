# Author: Madhu Chakravarthy
# Date: 20-04-2017

def fibonacci_series(n):

    series = []

    def fibonacci_series2(i, series):
        if i == 0:
            series.append(0)
            return
        if i == 1:
            series.extend([0,1])
            return
        fibonacci_series2(i - 1, series)
        series.append(series[len(series) - 1] + series[len(series) - 2])
    fibonacci_series2(n,series)
    return series

print fibonacci_series(0)
print fibonacci_series(1)
print fibonacci_series(2)
print fibonacci_series(3)
print fibonacci_series(4)
print fibonacci_series(5)
print fibonacci_series(6)
print fibonacci_series(7)
