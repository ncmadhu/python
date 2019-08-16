import unittest
import random

def random_index_gen(start, end):
    return random.randrange(start, end + 1)

def shuffle(input_list):
    length = len(input_list)
    if length <= 1:
        return input_list

    last_index = length - 1
    for index in range(0, length - 1):
        random_index = random_index_gen(index, last_index)
        if random_index != index:
            input_list[index], input_list[random_index] = input_list[random_index], input_list[index]
    print(input_list)
    return input_list

class TestCase(unittest.TestCase):
    def testcase(self):
        self.assertNotEqual([1,2,3,4,5], shuffle([1,2,3,4,5]))


if __name__ == '__main__':
    unittest.main()

