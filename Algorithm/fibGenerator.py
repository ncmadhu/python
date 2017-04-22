# Author: Madhu Chakravarthy
# Date: 22-04-2017

def fibanocciGenerator(num):

    a,b = 0,1

    for i in xrange(0,num):
        print "Gen"
        yield "{}: {}".format(i + 1, a)
        a,b = b, a+b


fibGen = fibanocciGenerator(8)
print fibGen.next()
print fibGen.next()
print fibGen.next()
print fibGen.next()
print fibGen.next()
print fibGen.next()
print fibGen.next()
print fibGen.next()
