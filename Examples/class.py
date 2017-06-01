# Author: Madhu Chakravarthy
# Date: 2-06-2017

class OldClass:

    def __init__(self):
        print "Old Class"


class NewClass(object):

    def __init__(self):
        print "New Class"


if __name__ == "__main__":

    oc = OldClass()
    nc = NewClass()

    print type(oc)
    print type(nc)

    print isinstance(oc, OldClass)
    print isinstance(nc, NewClass)

    print type(oc) == OldClass
    print type(nc) == NewClass

