# Author: Madhu Chakravarthy
# Date: 27-07-2017

def diamond(length):

    print "{}{}{}".format(" " * (length/2), "*" , " " * (length/2))

    middle_space = 1

    for i in range(3,length,2):
        space = (length - 2 - middle_space) / 2
        print "{}{}{}{}".format(" " * space, "*", " " * middle_space, "*", " " * space)
        middle_space += 2

    print "{}{}{}".format("*"," " * (length - 2), "*") 

    for i in range(length,3,-2):
        middle_space -= 2
        space = (length - 2 - middle_space) / 2
        print "{}{}{}{}".format(" " * space, "*", " " * middle_space, "*", " " * space)

    print "{}{}{}".format(" " * (length/2), "*" , " " * (length/2))


if __name__ == "__main__":

    length = 3
    number = 4
    for i in range(0,number):
        diamond(length)
        length += 2






