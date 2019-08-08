#Author: Madhu Chakravarthy
#Date: 17-04-2018

def primalityTest(n):

    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i * i <= n:
        if n % i  == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True

if __name__ == "__main__":
    print primalityTest(11)
    print primalityTest(15)
