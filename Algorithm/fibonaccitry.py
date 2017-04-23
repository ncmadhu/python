def fibonacci(number):

    series = []
    def fibonacci_inner(i):

        if i == 0:
            series.append(0)
            return
        if i == 1:
            series.extend([0,1])
            return

        fibonacci_inner(i-1)
        length = len(series)
        series.append(series[length -1] + series[length -2])

    fibonacci_inner(number)
    print series

fibonacci(0)
fibonacci(1)
fibonacci(2)
fibonacci(3)
fibonacci(4)
fibonacci(5)
fibonacci(6)
fibonacci(7)
fibonacci(8)
