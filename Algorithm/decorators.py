# Author: Madhu Chakravarthy
# Date: 22-04-2017

def decorator(originalFunc):

    def wrapper(*args, **kwargs):

        return "Hi {}".format(originalFunc(*args, **kwargs))

    return wrapper

@decorator
def display(message):

    return "from display function {}".format(message)


print display("Madhu")


def decoratorWithArgs(arg1, arg2):

    def actualDecorator(originalFunc):

        def wrapper(*args,**kwargs):

            return "{} {} {}".format(arg1,arg2, originalFunc(*args, **kwargs))
        return wrapper

    return actualDecorator

@decoratorWithArgs("arg1", "arg2")
def display(message):

    return message

print display("Madhu")
