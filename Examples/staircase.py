# Author: Madhu Chakravarthy
# Date: 1-06-2017

def staircase(n):

    for i in range(1, n+1):
        print "{}".format("*" * i)

if __name__ == "__main__":
    staircase(5)
