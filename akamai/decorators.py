#Author: Madhu Chakravarthy
#Date: 19-04-2018
def decorator(originalFunc):
    def wrapper(*args, **kwargs):

        return "From decorator : {}".format(originalFunc(*args, **kwargs))
    return wrapper

@decorator
def display1(msg):
    print "From original func {}".format(msg)
    return "display1"


def decoratorWithArgs(arg1, arg2):
    def actualDecorator(originalFunc):
        def wrapper(*args, **kwargs):
            return "From decorator {} {} {}".format(arg1, arg2, originalFunc(*args, **kwargs))
        return wrapper
    return actualDecorator

@decoratorWithArgs("arg1", "arg2")
def display2(msg):
    print "From original func {}".format(msg)
    return "display2"


if __name__ == "__main__":
    print display1("decorator with no args")
    print display2("decorator with args")
