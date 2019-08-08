# Author: Madhu Chakravarthy
# Date: 23-04-2017

def palindromeCheck(word):

    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return palindromeCheck(word[1:-1])


def palindromeCheck2(word):

    length = len(word)
    isPalindrome =  True
    for i in range(length/2):

        if word[i] != word[length-1-i]:
            isPalindrome = False
            break
    return isPalindrome


print "malayalam: {}".format(palindromeCheck("malayalam"))
print "alayalam: {}".format(palindromeCheck("alayalam"))
print "abba: {}".format(palindromeCheck("abba"))
print "acba: {}".format(palindromeCheck("acba"))
print "malayalam: {}".format(palindromeCheck2("malayalam"))
print "alayalam: {}".format(palindromeCheck2("alayalam"))
print "abba: {}".format(palindromeCheck2("abba"))
print "acba: {}".format(palindromeCheck2("acba"))
