import unittest

class Solution:
    def unique_id(self, delivery_id_confirmations):
        id_dict = {}
        sum = 0
        for id in delivery_id_confirmations:
            if id in id_dict:
                sum -= id
                del id_dict[id]
            else:
                sum += id
                id_dict[id] = 1
        return sum

    def unique_id_2(self, delivery_id_confirmations):
        unique_id = 0
        for id in delivery_id_confirmations:
            unique_id ^= id
        return unique_id


class Test(unittest.TestCase):

    def test1(self):
        solution = Solution()
        self.assertEqual(solution.unique_id([1,2,3,4,5,3,1,4,5]), 2)

    def test2(self):
        solution = Solution()
        self.assertEqual(solution.unique_id_2([1,2,3,4,5,3,1,4,5]), 2)

if __name__ == '__main__':
    unittest.main()