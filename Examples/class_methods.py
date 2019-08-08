# Author: Madhu Chakravarthy
# Date: 27-07-2017

class ParentClass(object):

    @staticmethod
    def stat_method():
        print "Static Method"

    @classmethod
    def class_method(cls):
        print "Class Method"


class ChildClass(ParentClass):

    @staticmethod
    def stat_method():
        print "Static Method from Child"

    @classmethod
    def class_method(cls):
        print "Class Method from child"


class SecondChild(ParentClass):
    pass


if __name__ == "__main__":

    pc = ParentClass()

    pc.class_method()

    pc.stat_method()

    cc = ChildClass()

    cc.class_method()

    cc.stat_method()

    ParentClass.class_method()
    ParentClass.stat_method()

    ChildClass.class_method()
    ChildClass.stat_method()

    SecondChild.class_method()
    SecondChild.stat_method()
