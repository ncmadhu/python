# Author: Madhu Chakravarthy
# Date: 10-04-2017

def maxandnextmax(input):

    max = input[0]
    max2 = input[1]
    for i in range(len(input) -1):

        if input[i] > max:
            max = input[i]
        if input[i + 1] > max2:
            max2 = input[i + 1]

        if max2 > max:
            max, max2 = max2, max
    return max, max2


print maxandnextmax([4,2,5,3])
print maxandnextmax([20,67,3,2.6,7,74,2.8,90.8,52.8,4,3,2,5,7])