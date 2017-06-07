# Author: Madhu Chakravarthy
# Date: 07-06-2017

from itertools import islice

def highestProductOf3(list):

    if len(list) < 3:
        print "Less than 3 items"
        return

    highest = max(list[0],list[1])
    lowest = min(list[0],list[1])

    highestProductOf2 = highest * lowest

    lowestProductOf2 = highest * lowest

    highestProductOf3 = highestProductOf2 * list[2]
    

    for current in islice(list, 2, None):


        highestProductOf3 = max(highestProductOf3,
                                highestProductOf2 * current,
                                lowestProductOf2 * current)

        highestProductOf2 = max(highestProductOf2,
                                current * highest,
                                current * lowest)


        lowestProductOf2 = min(lowestProductOf2,
                               current * highest,
                               current * lowest)


        highest = max(highest, current)
        lowest = min(lowest, current)

    print highestProductOf3



if __name__ == "__main__":

    highestProductOf3([1, 10, -5, 1, -100])


                               




