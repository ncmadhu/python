# Author: Madhu Chakravarthy
# Date: 24-04-2017

def counter(maximum):

    i = 0
    while i < maximum:
        val = yield i
        if val is not None:
            i = val
        else:
            i += 1

cntr = counter(10)

print cntr.next()
print cntr.next()
print cntr.send(4)
print cntr.next()
