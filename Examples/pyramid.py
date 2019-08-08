# Author: Madhu Chakravarthy
# Date: 1-06-2017


def uppyramid(n):

    x = n + (n -1)
    y = 1
    for i in range(n):
        print "{}{}{}".format(" " * ((x - y) / 2),
                              "*" * y,
                              " " * ((x - y) / 2))
        y += 2

def downpyramid(n, diamond = False):

    x = n + (n -1)
    y = x
    if diamond:
        n = n - 1
        y -= 2
    for i in range(n,0,-1):
        print "{}{}{}".format(" " * ((x - y) / 2),
                              "*" * y,
                              " " * ((x - y) / 2))
        y -= 2


def diamond(n):
    uppyramid(n)
    downpyramid(n, True)


if __name__ == "__main__":

    #uppyramid(5)
    #downpyramid(5)
    diamond(5)
    diamond(5)
