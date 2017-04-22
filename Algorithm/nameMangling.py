# Author: Madhu Chakravarthy
# Date: 20-04-2017

class MyClass(object):

    __hiddenVariable = "HV"
    publicVariable = "PV"

    def __init__(self):

        self.instanceVariable = "test"

    @classmethod
    def getHv(cls):
        return cls.__hiddenVariable


if __name__ == "__main__":

    myClass = MyClass
    print myClass.publicVariable
    print MyClass.publicVariable

    print myClass.getHv()
    print myClass._MyClass__hiddenVariable

    # Errors
    try:
        print myClass.__hiddenVariable
    except Exception as e: 
        print e

    try:
        print MyClass.__hiddenVariable
    except Exception as e:
        print e
