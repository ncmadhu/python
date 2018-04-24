#Author: Madhu Chakravarthy
#Date: 19-04-2018

def quickSort(unsortedList):

    length = len(unsortedList)

    if length <= 1:
        return unsortedList

    pivot = unsortedList.pop(0)

    left = []
    right = []
    for num in unsortedList:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    left = quickSort(left)
    right = quickSort(right)

    return left + [pivot] + right


if __name__ == "__main__":

    print quickSort([100,150,34,30,12,55,1,122,10,20,2,35,32,56,23,89,33,55,11,0])

