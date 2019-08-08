#!/bin/python
# Author: Madhu Chakravarthy
# Date: 1-1-2018

class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def char_to_index(self,char):
        return ord(char) - ord('a')

    def insert(self, word):
        parent_node = self.root
        word_length = len(word)
        for index in range(word_length):
            char = word[index]
            char_index = self.char_to_index(char)
            if not parent_node.children[char_index]:
                parent_node.children[char_index] = self.get_node()
            parent_node = parent_node.children[char_index]
        parent_node.end_of_word = True

    def search(self, word):
        parent_node = self.root
        word_length = len(word)
        for index in range(word_length):
            char = word[index]
            char_index = self.char_to_index(char)
            if not parent_node.children[char_index]:
                return False
            parent_node = parent_node.children[char_index]
        return parent_node.end_of_word

if __name__ == "__main__":
    words = ["test", "words", "within", "a", "list", "and"]
    search_words = words[0:2] + ["not"]  + words[2:] + ["present", "word"]

    trie = Trie()

    for word in words:
        trie.insert(word)

    for word in search_words:
        print trie.search(word)
