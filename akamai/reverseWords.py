#Author: Madhu Chakravarthy
#Date: 18-04-2018
def reverseWords(sentence):

    s = list(sentence)
    length = len(s)
    start = 0
    i = 0

    while i < length:
        while i < length and s[i] != ' ':
            i += 1

        reverse(s, start, i)
        i += 1
        start = i

    return "".join(s)

def reverse(word, start, end):
    middle = (start + end) / 2
    i = start
    right = end
    while i < middle:
        right -= 1
        word[i], word[right] = word[right], word[i]
        i += 1

if __name__ == "__main__":
    print reverseWords("The sky is blue")


