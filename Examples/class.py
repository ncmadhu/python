# Author: Madhu Chakravarthy
# Date: 2-06-2017

class OldClass:

    def __init__(self):
        print "Old Class initiated"


class NewClass(object):

    def __init__(self):
        print "New Class initiated"


if __name__ == "__main__":

    oc = OldClass()
    nc = NewClass()

    print "OldClass type: {}".format(type(oc))
    print "NewClass type: {}".format(type(nc))

    print "oc is instance of OldClass: {}".format(isinstance(oc, OldClass))
    print "oc is instance of object: {}".format(isinstance(oc, object))
    print "nc is instance of NewClass: {}".format(isinstance(nc, NewClass))
    print "nc is instance of object: {}".format(isinstance(nc, object))

    print "oc type equals OldClass: {}".format(type(oc) == OldClass)
    print "nc type equals NewClass: {}".format(type(nc) == NewClass)

