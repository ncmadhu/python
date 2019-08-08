#Author: Madhu Chakravarthy
#Date: 17-04-2018
def reciprocalOfLetters(word):

    start = ord('A')
    end = ord('Z')

    reciprocal = ""

    for char in word:

        fromA = ord(char) - start
        reciprocalChar = chr(end - fromA)
        reciprocal += reciprocalChar

    return reciprocal

if __name__ == "__main__":
    print reciprocalOfLetters('PRAKHAR')

