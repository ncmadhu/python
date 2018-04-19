#Author: Madhu Chakravarthy
#Date: 17-04-2018
def pxpy(arr):
    """
    largest x where arr[x] < arr[x+1]
    largest y where arr[x] < arr[y]
    """
    largestI = -1

    for i in range(len(arr) - 1):

        if arr[i] < arr[i+1]:
            largestI = i

    largestJ = -1

    for j in range(len(arr)):
        if arr[largestI] < arr[j]:
            largestJ = j

    print largestI
    print largestJ

if __name__ == "__main__":
    pxpy([0,1,2,3,4,5])
