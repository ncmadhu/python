#Author: Madhu Chakravarthy
#Date: 29-07-2019

def plus_one(digits):
    length = len(digits)
    sum = 0
    for index, value in enumerate(digits):
        sum = sum + (10 ** (length - 1 - index) * value)
    sum = sum + 1
    return_value = []
    while sum > 0:
        return_value.insert(0, sum % 10)
        sum = sum / 10
    return return_value


if __name__ == "__main__":
    print plus_one([4,7,3])

