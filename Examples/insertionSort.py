# Author: Madhu Chakravarthy
# Date: 09-01-2018

def insertionSort(unsortedList):

    length = len(unsortedList)

    for i in range(1, length):
        valueToInsert = unsortedList[i]
        insertPos = i

        while insertPos > 0  and unsortedList[insertPos - 1] > valueToInsert:
            unsortedList[insertPos] = unsortedList[insertPos - 1]
            insertPos -= 1
        unsortedList[insertPos] = valueToInsert

    return unsortedList


if __name__ == "__main__":
    print insertionSort([14,33,27,10,35,19,42,44])
