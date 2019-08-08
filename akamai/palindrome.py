#Author: Madhu Chakravarthy
#Date: 19-04-2018
def palindromeCheck(string):

    length = len(string)

    for i in range(length/2):
        if string[i] != string[length - 1 - i]:
            return False
    return True

if __name__ == "__main__":
    print palindromeCheck("malayalam")
    print palindromeCheck("abba")
    print palindromeCheck("test")
