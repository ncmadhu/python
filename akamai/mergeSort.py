#Author: Madhu Chakravarthy
#Date: 19-04-2018

def mergeSort(unsortedList):
    length = len(unsortedList)

    if length <=1:
        return unsortedList

    middle = length / 2
    ul1 = unsortedList[:middle]
    ul2 = unsortedList[middle:]

    l1 = mergeSort(ul1)
    l2 = mergeSort(ul2)

    return merge(l1,l2)

def merge(l1, l2):

    c = []
    while l1 and l2:
        if l1[0] > l2[0]:
            c.append(l2.pop(0))
        else:
            c.append(l1.pop(0))

    if l1:
        c.extend(l1)

    if l2:
        c.extend(l2)

    return c

if __name__ == "__main__":
    print mergeSort([88, 32, 12, 54, 95, 1, 55, 0])

