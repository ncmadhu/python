# Author: Madhu Chakravarthy
# Date: 24-04-2017

print "Max: {}".format(reduce(lambda x,y: x if x > y else y, [45,54,66,22]))
print "Min: {}".format(reduce(lambda x,y: x if x < y else y, [45,54,66,22]))

