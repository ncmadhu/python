import unittest

def reverse_string(string):

    left_index = 0
    right_index = len(string) - 1

    list_of_ch = list(string)

    while left_index < right_index:
        list_of_ch[left_index], list_of_ch[right_index] = list_of_ch[right_index], list_of_ch[left_index]
        left_index += 1
        right_index -= 1

    return "".join(list_of_ch)

class TestCase(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(reverse_string("malayalam"), "malayalam")

    def testcase2(self):
        self.assertEqual(reverse_string("mala"), "alam")

if __name__ == "__main__":
    unittest.main()