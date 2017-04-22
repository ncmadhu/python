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

