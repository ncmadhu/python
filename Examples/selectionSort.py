# Author: Madhu Chakravarthy
# Date: 09-01-2018

def selectionSort(unsortedList):

    length =  len(unsortedList)

    for i in range(length - 1):
        min = i
        for j in range(i+1, length):
            if unsortedList[min] > unsortedList[j]:
                min = j
        if min != i:
            unsortedList[i],unsortedList[min] = unsortedList[min],unsortedList[i]
    return unsortedList

if __name__ == "__main__":

    print selectionSort([14,33,27,10,35,19,42,44])
