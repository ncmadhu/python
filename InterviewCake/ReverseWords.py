import unittest

def reverse_characters(char_list, left_index, right_index):
    while left_index < right_index:
        char_list[left_index], char_list[right_index] = char_list[right_index], char_list[left_index]
        left_index += 1
        right_index -= 1

def reverse_words(sentence):

    sentence_list = list(sentence)
    sentence_length = len(sentence)
    reverse_characters(sentence_list, 0, sentence_length - 1)

    left_index = 0
    right_index = 0
    while left_index < sentence_length:
        if right_index == sentence_length or sentence_list[right_index] == " ":
            reverse_characters(sentence_list, left_index, right_index - 1)
            left_index = right_index = right_index + 1
        else:
            right_index += 1
    return "".join(sentence_list)

class Testcase(unittest.TestCase):
    def test1(self):
        self.assertEqual(reverse_words("cake pound steal"), "steal pound cake")

if __name__ == "__main__":
    unittest.main()