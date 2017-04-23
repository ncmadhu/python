# Author: Madhu Chakravarthy
# Date: 23-04-2017

def bubbleSort(ulist):

    for count in range(len(ulist) - 1, 0, -1):

        exchanged =  False

        for i in range(count):

            if ulist[i] > ulist[i + 1]:
                ulist[i], ulist[i + 1] = ulist[i + 1], ulist[i]
                exchanged =  True

        if not exchanged:
            break

    return ulist


print bubbleSort([5,8,2,1])
print bubbleSort([5])
print bubbleSort([])
print bubbleSort([1,2,3,4])
print bubbleSort([34,1,23,2,2])
