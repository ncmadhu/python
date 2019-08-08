#Author: Madhu Chakravarthy
#Date: 17-04-2018

def permutation(word):
    chosen = ''
    wordColl = set()
    wordList = list(word)
    printPermutation(wordList,chosen, wordColl)
    print wordColl

def printPermutation(wordList, chosen, wordColl):
    if not wordList:
        wordColl.add(chosen)
    for char in wordList:
        charIndex = wordList.index(char)
        wordList.remove(char)
        printPermutation(wordList, chosen+char, wordColl)
        wordList.insert(charIndex, char)


if __name__ == "__main__":
    permutation("abcd")
    permutation("aa")
