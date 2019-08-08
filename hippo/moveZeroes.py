#Author: Madhu Chakravarthy
#Date: 26-09-2019

def move_zeroes(numbers):
    index = 0
    zero_list = []
    for i in range(len(numbers)):
        if not numbers[index]:
            numbers.pop(index)
            zero_list.append(0)
        else:
            index += 1
    numbers.extend(zero_list)

if __name__ == "__main__":
    numbers = [0, 0, 1, 2, 0, 3, 0, 4]
    move_zeroes(numbers)
    print numbers
