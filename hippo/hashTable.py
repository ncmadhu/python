#Author: Madhu Chakravarthy
#Date: 31-08-2019

class Item(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_func(self, key):
        return key % self.size

    def set(self, key, value):
        hash_index =  self._hash_func(key)
        for item in self.table[hash_index]:
            if item.key == key:
                item.value = value
                return
        self.table[hash_index].append(Item(key, value))

    def get(self, key):
        hash_index = self._hash_func(key)
        for item in self.table[hash_index]:
            if item.key == key:
                return item.value
        raise KeyError("Key not found")

    def remove(self, key):
        hash_index = self._hash_func(key)
        for index, item in enumerate(self.table[hash_index]):
            if item.key == key:
                del self.table[hash_index][index]
                return
        raise KeyError("Key not found")

if __name__ == "__main__":
    ht = HashTable(5)
    ht.set(10, "Ten")
    print ht.get(10)
    ht.set(10, "TenTen")
    print ht.get(10)
    ht.set(11, "Eleven")
    print ht.get(11)
    ht.set(20, "Twenty")
    print ht.get(20)
    print ht.get(10)
    ht.remove(10)
    print ht.get(10)



