# Author: Madhu Chakravarthy
# Date: 24-04-2017


from collections import defaultdict

def charCount(string):

    count = defaultdict(int)

    for char in string:
        count[char] += 1
    return count


print charCount('abcdefgabc')



