#!/bin/python
# Author: Madhu Chakravarthy
# Date: 21-12-2017

def findMissingNumberCount(listA, listB):

    listANumCount = buildNumberCountDict(listA)
    listBNumCount = buildNumberCountDict(listB)
    missingNumList = []
    for num in listBNumCount:
        diff = listBNumCount[num] - listANumCount.get(num,0)
        if diff > 0:
            missingNumList.append(num)

    return missingNumList


def buildNumberCountDict(numList):

    numCountDict = {}
    for num in numList:
        numCountDict[num] = numCountDict.get(num, 0) + 1

    return numCountDict

if __name__ == "__main__":
    missingNumList = findMissingNumberCount([207,203,204,205,206,207,208,203,204,205,206],
            [207,203,204,204,205,206,207,205,208,203,206,205,206,204])
    

