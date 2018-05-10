#Author: Madhu Chakravarthy
#Date: 09-05-2018
def oddStrings(strArr, m):

    sum = 0

    for string in strArr:
        prod = 1
        for char in string:
            prod = prod * ord(char) ** m

        sum += prod

    return sum

if __name__ == "__main__":
    strArr = ['ab']
    m = 2
    print oddStrings(strArr, m)
    strArr = ['ab', 'ac', 'de']
    m = 50
    print oddStrings(strArr, m)


