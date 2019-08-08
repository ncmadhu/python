# Author: Madhu Chakravarthy
# Date: 22-04-2017

def anagramCheck(str1, str2):

    str2_list = list(str2)
    anagram = True

    for i in range(len(str1)):
        found =  False
        for j in range(len(str2_list)):
            if str1[i] == str2_list[j]:
                found = True
                str2_list[j] = None
                break
        if not found:
            anagram = False
            break
    return anagram


print anagramCheck("abcd", "dcba")
print anagramCheck("abcd", "dccba")
print anagramCheck("wxyz", "wxya")
