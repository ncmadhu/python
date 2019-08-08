# Enter your code here. Read input from STDIN. Print output to STDOUT
#primality tests
def isPrime(n):
    if n <= 1:
        return "Not prime"
    elif n <= 3:
        return "Prime"
    elif (n % 2 == 0) or (n % 3 == 0):
        return "Not prime"
    i = 5
    while i*i <= n:
        if (n % i == 0) or (n % (i + 2) == 0):
            return "Not prime"
        i = i + 6
    return "Prime"

t = int(raw_input().strip())
for i in range(t):
    n = int(raw_input().strip())
    print isPrime(n)