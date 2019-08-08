#Author: Madhu Chakravarthy
#29-07-2019
def twoSum(numbers, target):
    map = {}
    for index, value in enumerate(numbers):
        complement = target - value
        if complement in map:
            return [map[complement], index]
        map[value] = index

if __name__ == "__main__":
    print twoSum([2,7,11,15], 9)
