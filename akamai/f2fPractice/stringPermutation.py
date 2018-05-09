#Author: Madhu Chakravarthy
#Date: 01-05-2018

def permute(word):
    chosen = ''
    result = []
    permuteHelper(list(word), chosen, result)
    return result


def permuteHelper(charList,chosen, result):
    if not charList:
        result.append("".join(chosen))

    for i, char in enumerate(charList):
        charList.pop(i)
        permuteHelper(charList, chosen+char, result)
        charList.insert(i, char)


if __name__ == "__main__":
    print permute("abcd")
    print permute("abcc")


